import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

import creategraph
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
    # otherwise in the dual phase
    if np.sum(path_list == p) == 1:
        flow[p][q] = flow[p][q] + min(max_kilter, maxflow)
        kilter[p][q] = calculate_kilter_number(flow, upper, lower, p, q, reduced_cost[p][q])
        for i in range(len(path_list) - 1):
            a = path_list[i]
            b = path_list[i + 1]
            if original[a][b] == 1:
                flow[a][b] = flow[a][b] + min(max_kilter, maxflow)
                kilter[a][b] = calculate_kilter_number(flow, upper, lower, a, b, reduced_cost[a][b])
            else:
                flow[b][a] = flow[b][a] - min(max_kilter, maxflow)
                kilter[b][a] = calculate_kilter_number(flow, upper, lower, b, a, reduced_cost[b][a])
    # DUAL PHASE
    else:
        Xlist = np.where(visited == 1)[0]
        theta_1 = 99999
        theta_2 = 99999
        for i in range(nodes):
            for j in range(nodes):
                if i in Xlist and j not in Xlist and reduced_cost[i][j] < 0 and flow[i][j] <= upper[i][j]:
                    theta_1 = min(theta_1, -reduced_cost[i][j])
                elif i not in Xlist and j in Xlist and reduced_cost[i][j] > 0 and flow[i][j] >= lower[i][j]:
                    theta_2 = min(theta_2, reduced_cost[i][j])
        if theta_1 == 99999:
            print("No feasible solution to primal problem")
            break
        else:
            theta = min(theta_1, theta_2)
            for i in range(nodes):
                for j in range(nodes):
                    if i in Xlist and j not in Xlist:
                        reduced_cost[i][j] += theta
                        kilter[i][j] = calculate_kilter_number(flow, upper, lower, i, j, reduced_cost[i][j])
                    elif i not in Xlist and j in Xlist:
                        reduced_cost[i][j] -= theta
                        kilter[i][j] = calculate_kilter_number(flow, upper, lower, i, j, reduced_cost[i][j])

    print("FLOW: ", flow)
    print("Reduced Costs", reduced_cost)
    cost_associate = np.sum(cost * flow)
    print("Associated Costs: ", str(cost_associate))
    print("Number of Iterations: " + str(iterations))
