import numpy as np
import networkx as nx


def create_graph():
    with open("graph2.txt", 'r') as file:
        lines = file.readlines()

    visual_graph = nx.DiGraph()

    num_nodes = int(lines[0].strip())
    costs = np.zeros((num_nodes, num_nodes))
    upper = np.zeros((num_nodes, num_nodes))
    lower = np.zeros((num_nodes, num_nodes))

    for line in lines[1:]:
        source, destination, lb, ub, cost = map(int, line.strip().split())
        if not visual_graph.has_node(source):
            visual_graph.add_node(source)
        if source != num_nodes:
            visual_graph.add_edge(source, destination, first=ub, second=cost)

        costs[source - 1][destination - 1] = cost
        upper[source - 1][destination - 1] = ub
        lower[source - 1][destination - 1] = lb
    values = [costs, upper, lower, visual_graph]
    return values
