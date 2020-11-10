# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:21:28 2020

@author: Micky

"""
coordinate = []

        

board_numbers = range(1,16)                 
board = []
for i in range(3): #put 4 in row
  board.append([])
  for j in range(4): # put 4 in column
   board[i].append(coordinate) # add [] each spot


def print_board(board):
  for i in board:
     
     print (' '.join(map(str, i)))      
print(print_board(board))     #print the board


