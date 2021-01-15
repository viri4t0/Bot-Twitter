# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:22:52 2020

@author: Viriato
"""

import pytumblr
import json
import time
import datetime
import os
import requests






from random import randrange



#######################VARIABLES GLOBALES SEMILLA #############################
dir = os.path.dirname(__file__)
unano = 1225544552
creacion = 1193922152
#actual int(time.time())
nclaves = 2
#cuantos str desde el inicio de claves seran consideradas claves primarias
claves = [line.rstrip('\n') for line in open(dir+'/claves.txt')]



#################### FUNCIONES ################################################

def randomtime():
    number = randrange(unano, int(time.time()))
    return number

def randomclave():
    number = randrange(0, len(claves))
    return claves[number]


def buscarfotos(number):
    client = pytumblr.TumblrRestClient('**************************************************')
    ret = []
    tagcounter = 0
    contador = 0
    flag = randomclave()
    while len(ret) == 0:
        contador += 1
        if contador == 20:
            return 'none'
        listafotos = client.tagged(flag,before=randomtime())
        for foto in listafotos:
            tagcounter = 0
            if foto['type'] == 'photo':
                for tag in foto['tags']:
                    for mytag in claves:
                        if tag == mytag and mytag != flag:
                            tagcounter +=1
                            if tagcounter == number:
                                ret.append(foto)
                                break
                    else:
                        continue
                    break

    
    return ret

# ####################### MAIN ##################################################
    
def main():

    if not os.path.exists(dir+'/'+str(datetime.datetime.now().date())):
        os.mkdir(dir+'/'+str(datetime.datetime.now().date()))
    
     
    
    #registros diarios
    registrodiario = open(dir+'/'+str(datetime.datetime.now().date())+'/listaordenada.txt', "a")
    registrourldiario = open(dir+'/'+str(datetime.datetime.now().date())+'/listaordenadaurl.txt', "a")   
    
    #registros totales
    if not os.path.exists(dir+'/'+'registroblog.txt'):
        open(dir+'/'+'registroblog.txt', 'w').close()
    
    if not os.path.exists(dir+'/'+'registrourl.txt'):
        open(dir+'/'+'registrourl.txt', 'w').close()
    
    #variables main
    countimg = 00
    blogexiste = False
    urlexiste = False

    #loop principal 23 fotos 1 para cada hora 
    while countimg < 24:
        lista = buscarfotos(nclaves)
        if lista != 'none':
            for blog in lista:
                blogexiste = False
                with open(dir+'/'+'registroblog.txt', "r") as registroblog:
                    for line in registroblog:
                        if line == str(blog['id'])+'\n':
                            blogexiste = True;
                            break
                
                if blogexiste == False:        
                    
                    
                    registrodiario.write(str(countimg)+' '+str(blog['id'])+'\n')
                    with open(dir+'/'+'registroblog.txt', "a") as registroblog:
                        registroblog.write(str(blog['id'])+'\n')
                    with open(dir+'/'+str(datetime.datetime.now().date())+'/'+str(blog['id'])+'.json', 'w', encoding='utf-8') as f:
                        json.dump(blog, f, ensure_ascii=False, indent=4)
                    
                    
                    photo = blog['photos'][0]
                    urlexiste = False
                    with open(dir+'/'+'registrourl.txt', "r") as registrourl:
                        for url in registrourl:
                            if url == photo['original_size']['url']+'\n':
                                urlexiste=True
                                break
                    
                    if urlexiste == False:  
                        with open(dir+'/'+'registrourl.txt', "a") as registrourl:
                            registrourl.write(photo['original_size']['url']+'\n')
                        
                        imagen = requests.get(photo['original_size']['url']).content
                        split = photo['original_size']['url'].split(".")
                        registrourldiario.write(str(blog['id'])+'-'+str(countimg)+'.'+split[len(split)-1]+'\n')
                        with open(dir+'/'+str(datetime.datetime.now().date())+'/'+str(blog['id'])+'-'+str(countimg)+'.'+split[len(split)-1], 'wb') as handler:
                            handler.write(imagen)
                            countimg +=1
                        
    registrodiario.close()
    registrourldiario.close()

if __name__ == "__main__":
    main()