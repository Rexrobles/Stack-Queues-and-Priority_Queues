# This program will load the graph from a sample DOT file and store the result in two variables.
from graph import City, load_graph

# The load_graph inherits parameters from the graph.py file.
nodes, graph = load_graph("roadmap.dot", City.from_dict)
print(f"\n{nodes['london']}\n")