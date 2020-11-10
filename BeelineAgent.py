# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:16:33 2020

@author: Micky
"""

import action
from random import randint

agent_action = randint(0,6) 
if agent_action  ==  0:
        action.straight
elif agent_action  == 1:
        action.left
elif  agent_action  == 2:
        action.right
elif agent_action  == 3:
        action.shoot


