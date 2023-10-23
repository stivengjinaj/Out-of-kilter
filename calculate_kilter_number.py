def calculate_kilter_number(flow, u, l, i, j, zc):
    if zc < 0 or (zc == 0 and flow[i][j] < l[i][j]):
        val = abs(flow[i][j] - l[i][j])
    elif zc > 0 or (zc == 0 and flow[i][j] > u[i][j]):
        val = abs(flow[i][j] - u[i][j])
    else:
        val = 0

    if zc < 0:
        val2 = abs(flow[i][j] - l[i][j])
    elif zc > 0:
        val2 = abs(flow[i][j] - u[i][j])
    elif zc == 0 and flow[i][j] > u[i][j]:
        val2 = abs(flow[i][j] - u[i][j])
    elif zc == 0 and flow[i][j] < l[i][j]:
        val2 = abs(flow[i][j] - l[i][j])
    else:
        val2 = 0

    if val != val2:
        print('FAIL:', val, 'vs', val2)

    return val
