# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:16:33 2020

@author: Micky
"""

import action
from random import randint

def NextAction():
   
    r = randint(6) 
    if r ==  0:
        action.Forward
    elif r == 1:
        action.TurnLeft
    elif  r == 2:
        action.TurnRight
    elif r == 3:
        action.Shoot
    elif r == 4:
        action.grab
    elif r == 5:
        action.climb
   

