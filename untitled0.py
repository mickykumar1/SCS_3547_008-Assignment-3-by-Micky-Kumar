# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:14:55 2020

@author: Micky
"""

from pomegranate import *

wdN = DiscreteDistribution({ True: 1./15, False: 14./15 })
wdE = DiscreteDistribution({ True: 1./15, False: 14./15 })
wdS = DiscreteDistribution({ True: 1./15, False: 14./15 })
wdW = DiscreteDistribution({ True: 1./15, False: 14./15 })
wc = ConditionalProbabilityTable(
[[True, False, False, False, 1.0],
[False, True, False, False, 1.0],
[False, False, True, False, 1.0],
[False, False, False, True, 1.0],
[False, False, False, False, 0]],
[wdN, wdE ,wdS ,wdW])

s1 = State(wdN, name="s1")
s2 = State(wdE, name="s2")
s3 = State(wdN, name="s3")
s4 = State(wdN, name="s4")
s5 = State(wumpusConditional, name="s5")

model = BayesianNetwork()
model.add_states(s1, s5)
model.add_states(s2, s5)
model.add_states(s3, s5)
model.add_states(s4, s5)


model.add_edge(s1, s2)
model.add_edge(s2, s3)
model.add_edge(s3, s4)

model.bake()
print(model.probability)