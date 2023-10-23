import networkx as nx
from matplotlib import pyplot as plt


def update_plot(flow):
    with open("graph2.txt", 'r') as file:
        lines = file.readlines()

    updated_graph = nx.DiGraph()

    num_nodes = int(lines[0].strip())

    for line in lines[1:]:
        source, destination, lb, ub, cost = map(int, line.strip().split())
        if not updated_graph.has_node(source):
            updated_graph.add_node(source)

        if source != num_nodes:
            updated_graph.add_edge(source, destination, first=int(ub), second=int(flow[source-1][destination-1]))

    return updated_graph
