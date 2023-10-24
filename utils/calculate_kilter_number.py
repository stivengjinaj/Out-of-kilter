def calculate_kilter_number(flow, upper, lower, i, j, reduced_cost):
    if reduced_cost < 0 or (reduced_cost == 0 and flow[i][j] < lower[i][j]):
        val = abs(flow[i][j] - lower[i][j])
    elif reduced_cost > 0 or (reduced_cost == 0 and flow[i][j] > upper[i][j]):
        val = abs(flow[i][j] - upper[i][j])
    else:
        val = 0

    if reduced_cost < 0:
        val2 = abs(flow[i][j] - lower[i][j])
    elif reduced_cost > 0:
        val2 = abs(flow[i][j] - upper[i][j])
    elif reduced_cost == 0 and flow[i][j] > upper[i][j]:
        val2 = abs(flow[i][j] - upper[i][j])
    elif reduced_cost == 0 and flow[i][j] < lower[i][j]:
        val2 = abs(flow[i][j] - lower[i][j])
    else:
        val2 = 0

    if val != val2:
        print('FAIL:', val, 'vs', val2)

    return val
