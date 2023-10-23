import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

import creategraph
from dual_phase import dual_phase
from primal_phase import primal_phase
from update_graph import update_graph
from calculate_kilter_number import calculate_kilter_number
from dfs import dfs

values = creategraph.creategraph()

cost = values[0]
upper = values[1]
lower = values[2]

# Array used to keep track of visited nodes
visited = np.zeros(len(upper))
graph = np.zeros_like(upper)
nodes = upper.shape[0]
flow = np.zeros((nodes, nodes))

original = np.ones((nodes, nodes))

for i in range(nodes):
    for j in range(nodes):
        if upper[i, j] == lower[i, j] and lower[i, j] == 0:
            original[i, j] = 0

if np.sum((upper - lower) >= 0) != nodes * nodes:
    exit()

reduced_cost = -cost
kilter = np.zeros_like(upper)

for i in range(nodes):
    for j in range(nodes):
        kilter[i, j] = calculate_kilter_number(flow, upper, lower, i, j, reduced_cost[i, j])

iterations = 0

# The loop will continue until the sum of kilter numbers is 0
# or when there is no feasible solution.
while np.sum(np.sum(kilter)) != 0:
    iterations += 1

    print("Sum of kilter numbers: ", np.sum(np.sum(kilter)))

    # Find the greatest kilter number and start from there
    max_kilter = np.max(kilter)

    # Find the index of the greatest kilter number in a flattened array
    # Example:
    #  [[0. 0. 0. 0. 0. 0.]
    #  [5. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0.]
    #  [0. 0. 0. 0. 0. 0.]]
    #   The array will be flattened in the following way: 0 0 0 0 0 0 5 0 0 0 0 0......
    #   5 is in the 6-th position
    max_kilter_index = np.argmax(kilter)

    # Retrieve p and q from the index of the max kilter number
    p, q = np.unravel_index(max_kilter_index, kilter.shape)

    # Update graph with
    graph = update_graph(flow, upper, lower, reduced_cost)

    visited = np.zeros((nodes, 1))

    # Using Depth-First-Search algorithm, we find a path in the graph and
    # the maximum flow passing through that path
    maxflow, path_list = dfs(graph, q, p, 1000, [q], visited)

    # PRIMAL PHASE
    # If p is in the path we found using DFS, we enter the primal phase,
    # otherwise the dual phase
    if np.sum(path_list == p) == 1:
        primal_phase(flow, kilter, max_kilter, maxflow, p, q, path_list, upper, lower, reduced_cost, original)
    # DUAL PHASE
    else:
        dual_phase(flow, kilter, upper, lower, reduced_cost, nodes, visited)

    print("Iteration ", iterations, "Flow: \n", flow)
    print("Reduced Costs: \n", reduced_cost)

print("FINAL FLOW: \n", flow)
print("FINAL REDUCED COSTS\n", reduced_cost)
print("\n")
print("ASSOCIATED COST: ", np.sum(cost * flow))
print("TOTAL ITERATIONS: ", iterations)
