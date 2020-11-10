# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:21:28 2020

@author: Micky

"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.grid_2d_graph(5, 5)  # 4x4 grid

pos = nx.spring_layout(G, iterations=50)


plt.subplot(222)
nx.draw(G, pos, node_color="k", node_size=0, with_labels=False)


plt.show()