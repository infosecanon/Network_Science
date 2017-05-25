import random
import json

# Number of nodes to simulate
n = 100

# Generate a dict of random nodes
p = {(int)i: (random.uniform(0.0,100.0), random.uniform(0.0,100.0)) for i in range(n)}

# This can take a lot of time for 100k nodes, so save as json (memoization)
# This is going to save integer keys as strings, so we'll need to convert back
# to integer when reading the file back in
with open('nodes.json', 'w') as f:
    json.dump(p, f)
