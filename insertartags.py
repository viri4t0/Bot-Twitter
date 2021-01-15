# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:23:35 2020

@author: Viriato
"""

import os
import sys

dir = os.path.dirname(__file__)

def main(argv):
    
    if not os.path.exists(dir+'/claves.txt'):
        open(dir+'/claves.txt', 'w').close()
        
    listaclaves = [line.rstrip('\n') for line in open(dir+'/claves.txt','r')]
    
    if len(argv) == len(set(argv)):
        for arg in argv:
            for clave in listaclaves:
                if clave == arg:
                    break
            else:
                with open(dir+'/claves.txt','a') as apend:
                    apend.write(arg+'\n')
                continue
        
if __name__ == "__main__":
    main(sys.argv[1:])
                    
                    
    
    