import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy
import pylab as pl
import json

n = 100
radius = 30
nodes = {}

# Open our json file
with open('nodes.json', 'r') as f:
    nodes = json.load(f)

nodes_dict = {}

# Convert to integer keys
for key, value in nodes.iteritems():
    nodes_dict[int(key)] = [float(item) for item in value]
#print(nodes_dict)

G = nx.random_geometric_graph(n, radius, dim = 100, pos = nodes_dict)

# position is stored as node attribute data for random_geometric_graph
pos = nx.get_node_attributes(G, 'pos')

# find node near center (0.5,0.5)
dmin = 1
ncenter = 0
for n in pos:
    x,y = pos[n]
    d = (x-100)**2 + (y-100)**2
    if d < dmin:
        ncenter = n
        dmin = d

# color by path length from node near center
p = nx.single_source_shortest_path_length(G, ncenter)

plt.figure(figsize = (8,8))
nx.draw_networkx_edges(G, pos, nodelist=[ncenter], alpha=0.4)

nx.draw_networkx_nodes(G, pos, nodelist = p.keys(),
                       node_size = 80,
                       node_color = p.values(),
                       cmap = plt.cm.Reds_r)

# If you'd like to see the adjacency matrix
#A = nx.adjacency_matrix(G)
#print(A)
#print(A.todense())

# print degrees for nodes
#for n in G:
#    print(n, G.degree(n))

#degree = G.degree() # dictionary node:degree
#value = sorted(set(degree.values()))
#print(value)
#l = [degree.values().count(x) for x in value]

# Visualizations and Saving image
plt.axis([0, 100, 0, 100])
plt.savefig('random_geometric_graph_new30.png')
plt.grid(True)
plt.title('100x100 Random Field, d=30')
plt.show()
