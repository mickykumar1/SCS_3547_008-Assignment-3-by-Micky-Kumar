# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:42:53 2020

@author: Micky
"""
from random import choice, randint
import Performancemeasure, board, agent, ProbAgent, shortpath, Beelinestate

points = Performancemeasure.s_points

def main():

    wumpus_location = choice(board.board_numbers)
    agent_location = 1 #start at location 1
    gold = choice(board.board_numbers) # choice random spot for gold
    pit1 = choice(board.board_numbers) # choice random spot for pit
    pit2 = choice(board.board_numbers) # choice random spot for pit
    pit3 = choice(board.board_numbers) # choice random spot for pit
    climb = 1
    print("welcome to  wumpas world ")
    print("Created by Micky Kumar")
    print("You can see", len(board.board), "board" )
    print("To Play, just type the number")
    print("of the cave you wish to enter next")
    while True:
        print(" you are in board", agent_location)
        #if wumpus_location in caves[agent_location]:
        if (agent_location == wumpus_location -1 or
            agent_location == wumpus_location +1 ):
            print("I received a Stench. A wumpus is close by")
            print("There is a propability of wumpus by", ProbAgent.modelw.probability)
        if (agent_location == pit1 -1 or
            agent_location == pit1 +1 ):
            print("I  felt a breeze pit close by")
            print("There is a propability of pit close by of ", ProbAgent.pitprop.model.probability)
        if (agent_location == pit2 -1 or
            agent_location == pit2 +1 ):
            print("I  felt a breeze pit close by") 
            print("There is a propability of pit close by of", ProbAgent.pitprop.model.probability)
        if (agent_location == pit3 -1 or
            agent_location == pit3 +1 ):
            print("I  felt a breeze pit close by")                
        if (agent_location == gold -1 or
            agent_location == gold +1 ):
            print("gold close by") 
            print("Agent is getting ready to grab the gold")
        print("which cave next")
        al = randint(0,2)
        if al == BeelineAgent.agent_action: #Moving Forward
            agent_location+=1
            Beelinestate.safelocation.append(agent_location)
        elif al == BeelineAgent.agent_action: # Moving Left
            agent_location+=1
            Beelinestate.safelocation.append(agent_location)
        elif al == BeelineAgent.agent_action: # Moving Right
            agent_location+=1
            Beelinestate.safelocation.append(agent_location)
        elif al == BeelineAgent.agent_action: #Shoot Arrow
            agent_location-=1  
            Beelinestate.safelocation.append(agent_location)
        else:
            agent_location = int(al)
        if agent_location == wumpus_location:
            wa = randint(1,2)
            if wa == 1:
                        print(Performancemeasure.s_points-Performancemeasure.arrow)
                        print ("you killed the wumpus")
            elif wa == 2:
                    print(Performancemeasure.s_points-Performancemeasure.loss)
                    print("You got eaten by a wumpus")
                    break
        elif agent_location == pit1:
                print(Performancemeasure.s_points - Performancemeasure.loss)
                print("you fell in a pit")
                break
        elif agent_location == pit2:
                print(Performancemeasure.s_points - Performancemeasure.loss)
                print("you fell in a pit")
                break
        elif agent_location == pit3:
                print(Performancemeasure.s_points - Performancemeasure.loss)
                print("you fell in a pit")
                break            
        elif agent_location == gold:
            if True:
                print(Performancemeasure.s_points+Performancemeasure.win)
                print("Agent received the gold. You win!!!")
                print("Path to go back",Beelinestate.safelocation) # print the path to go back
                print("The shortest path is", shortpath.shortest_paths) #Show the shortest path using networkX
                break
            else:
                break
                
                
if __name__ == '__main__':
    main()
