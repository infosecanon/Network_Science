import networkx as nx
import matplotlib.pyplot as plt
import scipy
import pylab as pl
import numpy as np

def num_of_links():
	# Return a random float in (0.0, 1.0)
	die = np.random.random(1)

	if TEST == True:
		print (die)

	a = float(1)/3
	b = float(2)/3

	# Node generates 1 link
	if die < a:
		return 1

	# Node generates 2 links
	if die > a and die < b:
		return 2

	# Node generates 3 links
	if die > b:
		return 3

TEST = False

# Create initial network with 4 nodes
G = nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)

# Generate links between the nodes to make it a complete graph
G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)])

# Total number of nodes to add
num_of_nodes = 5000

# Iterate through the number of nodes to add
for n in range(5, num_of_nodes + 5):

	list_of_bad_nodes = []

	# How many nodes are currently in network G
	a = nx.number_of_nodes(G)

	# Generate a node
	if TEST == True:
		print ("Adding node ", n)
	G.add_node(n)

	if TEST == True:
		print ("Total nodes in G: ", a)

	# How many links will it form?
	# (Hardcode this to 3 when necessary)
	#links = num_of_links()
	links = 3
	
	if TEST == True:
		print ("Link #: ", links)

	# Calc the probability of each node
	total_links = nx.number_of_edges(G)



	while links > 0:
		# Iterate through the available nodes in G
		for iota,v in G.nodes(data=True):

			# Calculate the probability
			p = (float(G.degree(iota)) / total_links)

			if TEST == True:
				print ("Calculating probability.. ", p)

			# Return a random float in (0.0, 1.0)
			die = np.random.random(1)

			if TEST == True:
				print ("throw a die... ", die)

			if iota not in list_of_bad_nodes:


				# Add an edge between the new node and the examined node iff die < p
				if die < p:

					G.add_edge(iota,n)

					links = (links - 1)

					list_of_bad_nodes.extend([iota])

					if TEST == True:
						print ("link! links left = ", links)
					if links == 0:
						break
				else:
					if TEST == True:
						print ("no link...")

	if TEST == True:
		print("exited while... ")

# Calculating the number of nodes/edges in the network
#a = nx.number_of_nodes(G)
#b = nx.number_of_edges(G)

if TEST == True:
	print ("Total nodes in G: ", a)
if TEST == True:
	print ("Total edges in G: ", b)
if TEST == True:
	for n in G:
	    print(n, G.degree(n))

# Visualization
plt.figure(figsize=(10,10))
nx.draw(G,node_size=40)
#plt.savefig('BA_5k_links.png')
plt.show()