# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 21:34:44 2020

@author: Viriato
"""

import tweepy
import datetime
import os


def main():
    twitter_auth_keys = { 
        "consumer_key"        : "***************************",
        "consumer_secret"     : "****************************************************",
        "access_token"        : "****************************************************",
        "access_token_secret" : "****************************************************"
    }
 
    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)
 
    
    dir = os.path.dirname(__file__)
    # Upload image
    hora = datetime.datetime.now().strftime("%H")
    carpetaurl = str(datetime.datetime.now().date())
    registros = []
    with open(dir+'/'+carpetaurl+'/listaordenadaurl.txt', "r") as registroblog:
        registros = registroblog.readlines()
    
    media = api.media_upload(dir+'/'+carpetaurl+"/"+str(registros[int(hora)]).rstrip())
 
    # Post tweet with image
    post_result = api.update_status(media_ids=[media.media_id])
    with open(dir+'/'+str(datetime.datetime.now().date())+'/twitterlog-'+hora+'.txt', 'w') as f:
        f.write(str(post_result))
        
        
 
if __name__ == "__main__":
    main()