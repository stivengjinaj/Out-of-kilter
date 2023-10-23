import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def creategraph():
    with open("graph2.txt", 'r') as file:
        lines = file.readlines()

    visual_graph = nx.DiGraph()

    num_nodes = int(lines[0].strip())
    c = np.zeros((num_nodes, num_nodes))
    u = np.zeros((num_nodes, num_nodes))
    l = np.zeros((num_nodes, num_nodes))

    for line in lines[1:]:
        s, d, lb, ub, cost = map(int, line.strip().split())
        if not visual_graph.has_node(s):
            visual_graph.add_node(s)
        visual_graph.add_edge(s, d, upper=ub, cost=c)
        c[s - 1][d - 1] = cost
        u[s - 1][d - 1] = ub
        l[s - 1][d - 1] = lb

    values = [c, u, l, visual_graph]
    return values
