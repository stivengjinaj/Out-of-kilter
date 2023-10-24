def calculate_kilter_number(flow, upper, lower, i, j, reduced_cost):
    if reduced_cost < 0 or (reduced_cost == 0 and flow[i][j] < lower[i][j]):
        kilter_number = abs(flow[i][j] - lower[i][j])
    elif reduced_cost > 0 or (reduced_cost == 0 and flow[i][j] > upper[i][j]):
        kilter_number = abs(flow[i][j] - upper[i][j])
    else:
        kilter_number = 0

    return kilter_number
