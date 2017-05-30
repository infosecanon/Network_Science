import networkx as nx
import matplotlib.pyplot as plt
import scipy
import pylab as pl

# returns a random BA graph showing PA
# A graph of n nodes is grown by attaching new nodes each with m edges that are
# preferentially attached to existing nodes with high degree.

# n = number of nodes
# m = number of edges to attach from a new node to existing nodes

# seed (int, optional) - Seed for random number generator (default=None)

n = 100
m = 1
p = eval(open("100_nodes.txt").read())

#G=nx.barabasi_albert_graph(n, m, seed=None)
G=nx.barabasi_albert_graph(n, m, 0.5)

# print degrees for nodes
for n in G:
    print(n, G.degree(n))

# Visualizations and Saving image
plt.figure(figsize=(8,8))
nx.draw(G,node_size=80)
plt.savefig('BA_v1.png')
plt.show()
