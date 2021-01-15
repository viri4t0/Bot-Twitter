# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:01:55 2020

@author: Viriato
"""

import datetime
import json
import os
claves = ['camera','photography','landscapes','wallpaper','art','landscape','rain','forest','sea','wave','sunset','space','road','sky','rains','forests','seas','waves','sunsets','roads','skys','thunder','lightning','monuments','monument','moon','tree','trees','ocean','films','smoke','nature']

dir = os.path.dirname(__file__)
lineList = [line.rstrip('\n') for line in open(dir+'/claves.txt')]


#########COMPROBAR SI LINEA SE REPITE#################
with open(dir+'/claves.txt','r') as f:
    seen = set()
    for line in f:
        line_lower = line.lower()
        if line_lower in seen:
            print(line)
        else:
            seen.add(line_lower)
    





        
  