# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 12:11:27 2020

@author: Micky
"""

coordinate = [(1,1), (1,2), (1,3),(1,4),(2,1),(2,4),(3,1),(3,4), (4,1), (4,2), (4,3),(4,4)]

#coordinate = []
for y in range(0, 4):
    for x in range(0, 4):
        coordinate.append((x,y))
 
print(coordinate)
print(coordinate[0])