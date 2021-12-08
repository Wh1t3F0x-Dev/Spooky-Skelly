'''
 _____                 _           _____  _         _  _      
|   __| ___  ___  ___ | |_  _ _   |   __|| |_  ___ | || | _ _ 
|__   || . || . || . || '_|| | |  |__   || '_|| -_|| || || | |
|_____||  _||___||___||_,_||_  |  |_____||_,_||___||_||_||_  |
       |_|                 |___|                         |___|
Created by jfmartin1410
'''

'''
Configuraciones Previas
'''
#Importacion de las librerias o modulos
from core.core import *
from core.tools.submenu import *
#import random


'''
Menu INICIAL
'''

menu=submenu()
#nAle=random.randint(0,3)
menu.cmenu(banners.bannerList[3], menuTxt.msgIndex)
