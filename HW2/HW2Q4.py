import networkx as nx
import matplotlib.pyplot as plt
import scipy
import pylab as pl
import numpy as np

# Create initial network with 10 nodes
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)

# Generate links between the nodes to make it a complete graph
G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(5,4),(5,10),(6,7),(8,2),(9,1),(2,7),(6,3),(5,9)])

# Visualization
plt.figure(figsize=(10,10))
nx.draw(G,node_size=40)
plt.savefig('HW2Q4.png')
plt.show()
