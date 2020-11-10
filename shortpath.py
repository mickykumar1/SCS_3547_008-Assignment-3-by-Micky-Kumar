# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:05:28 2020

@author: Micky
"""

import networkx as na
import numpy as np


edges = [(1,1), (1,2), (1,3),(1,4),(2,1),(2,4),(3,1),(3,4), (4,1), (4,2), (4,3),(4,4)]

G = na.Graph()
G.add_edges_from(edges)
G.add_node(1)
shortest_paths = dict(na.shortest_path_length(G))
print(shortest_paths)
point_a = np.array((0,0,0))
point_b = np.array((1,1,1))

distance = np.linalg.norm(edges)
