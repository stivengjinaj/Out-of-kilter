import numpy as np

from utils.calculate_kilter_number import calculate_kilter_number


def primal_phase(flow, kilter, max_kilter, maxflow, p, q, path_list, upper, lower, reduced_cost, original):
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
                