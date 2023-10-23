import numpy as np


def update_graph(flow, upper, lower, reduced_cost):
    nodes, _ = flow.shape
    graph = np.zeros_like(flow)

    for i in range(nodes):
        for j in range(nodes):
            if reduced_cost[i][j] >= 0 and flow[i][j] < upper[i][j]:
                graph[i][j] = upper[i][j] - flow[i][j]
            if reduced_cost[i][j] <= 0 and flow[i][j] > lower[i][j]:
                graph[j][i] = flow[i][j] - lower[i][j]
            elif reduced_cost[i][j] < 0 and flow[i][j] < lower[i][j]:
                graph[i][j] = lower[i][j] - flow[i][j]
            elif reduced_cost[i][j] > 0 and flow[i][j] > upper[i][j]:
                graph[j][i] = flow[i][j] - upper[i][j]

    return graph
