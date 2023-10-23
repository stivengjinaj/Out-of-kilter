import numpy as np

from calculate_kilter_number import calculate_kilter_number


def dual_phase(flow, kilter, upper, lower, reduced_cost, nodes, visited):
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
        print("No feasible solution")
        exit()
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
