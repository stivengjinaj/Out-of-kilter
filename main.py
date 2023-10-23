import numpy as np

from create_graph import create_graph
from dual_phase import dual_phase
from primal_phase import primal_phase
from update_graph import update_graph
from calculate_kilter_number import calculate_kilter_number
from depth_first_search import depth_first_search
from plot_graph import plot_graph
from update_plot import update_plot

values = create_graph()

cost = values[0]
upper = values[1]
lower = values[2]

# Array used to keep track of visited nodes
visited = np.zeros(len(upper))
graph = np.zeros_like(upper)
nodes = upper.shape[0]
flow = np.zeros((nodes, nodes))
visual_graph = values[3]
plot_graph(visual_graph, "INITIAL GRAPH (capacity, cost)\n", "")
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
    #  The array will be flattened in the following way: 0 0 0 0 0 0 5 0 0 0 0 0......
    #  5 is in the 6-th position
    max_kilter_index = np.argmax(kilter)

    # Retrieve p and q from the index of the max kilter number
    p, q = np.unravel_index(max_kilter_index, kilter.shape)

    # Update graph with
    graph = update_graph(flow, upper, lower, reduced_cost)

    visited = np.zeros((nodes, 1))

    # Using Depth-First-Search algorithm, we find a path in the graph and
    # the maximum flow passing through that path
    maxflow, path_list = depth_first_search(graph, q, p, 1000, [q], visited)

    # If p is in the path we found using DFS, we enter the primal phase,
    # otherwise the dual phase
    # PRIMAL PHASE
    if np.sum(path_list == p) == 1:
        primal_phase(flow, kilter, max_kilter, maxflow, p, q, path_list, upper, lower, reduced_cost, original)
    # DUAL PHASE
    else:
        dual_phase(flow, kilter, upper, lower, reduced_cost, nodes, visited)

    print("Iteration:", iterations)
    print("Flow: \n\n", flow, "\n")
    print("Reduced Costs: \n\n", reduced_cost, "\n")

    # Uncomment to see all steps plotted
    # iteration_graph = update_plot(flow)
    # plot_graph(iteration_graph, "ITERATION: " + str(iterations) + " GRAPH (capacity, flow)\n", "Associated cost: " + str(np.sum(cost * flow)))

print("\n-------------- ALGORITHM COMPLETED. SOLUTION FOUND --------------\n")
print("FINAL FLOW: \n\n", flow, "\n")
print("FINAL REDUCED COSTS\n\n", reduced_cost, "\n")
print("\n")
print("ASSOCIATED COST: ", np.sum(cost * flow))
print("TOTAL ITERATIONS: ", iterations)

final_graph = update_plot(flow)
plot_graph(final_graph, "FINAL GRAPH (capacity, flow)\n", "Associated cost: " + str(np.sum(cost * flow)))
