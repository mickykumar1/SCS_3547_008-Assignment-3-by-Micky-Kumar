# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:16:33 2020

@author: Micky
"""
from pomegranate import *
import wumpusworld
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
        
# Below contain the probability of a wumpus        
# The direction has no node has no parents for wumpus
wdN = DiscreteDistribution({ True: 1./15, False: 14./15 })
wdE = DiscreteDistribution({ True: 1./15, False: 14./15 })
wdS = DiscreteDistribution({ True: 1./15, False: 14./15 })
wdW = DiscreteDistribution({ True: 1./15, False: 14./15 })
# Track wumpus  node is conditional on the location
wc = ConditionalProbabilityTable(
[[True, False, False, False, 1.0],
[False, True, False, False, 1.0],
[False, False, True, False, 1.0],
[False, False, False, True, 1.0],
[False, False, False, False, 0]],
[wdN, wdE ,wdS ,wdW])

# Create a Bayesian Network and add states

s1 = State(wdN, name="s1")
s2 = State(wdE, name="s2")
s3 = State(wdN, name="s3")
s4 = State(wdN, name="s4")
s5 = State(wc, name="s5")

modelw = BayesianNetwork()
modelw.add_states(s1, s5)
modelw.add_states(s2, s5)
modelw.add_states(s3, s5)
modelw.add_states(s4, s5)

# Add edges connecting nodes
modelw.add_edge(s1, s2)
modelw.add_edge(s2, s3)
modelw.add_edge(s3, s4)
# Finalize model for wumpus
modelw.bake()
print(modelw.probability)

def pitprop():
    # The probaility of a pit - true of false - .2 chance of a pit
    pitD = DiscreteDistribution({True: 0.20, False: 0.80})
    #Track pit  is conditional on the pit location
    PitC = ConditionalProbabilityTable(
    [[True, True, 1.0],
    [True, False, 1.0],
    [False, True, 1.0],
    [False, False,1.0]],
    [pitD])
    # Create a Bayesian Network and add states
    s1 = State(pitD, name="s1")
    s2 = State(PitC, name="s2")
    
    model = BayesianNetwork()
    model.add_states(s1, s2)
    # Add edges connecting nodes
    model.add_edge(s1, s2)
    # Finalize model for pit
    model.bake()
    probability = model.probability([["True"]])
    print(probability)
