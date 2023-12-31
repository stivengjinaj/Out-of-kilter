def depth_first_search(graph, source, destination, flow, path, visited):
    nodes = graph.shape[0]
    visited[source] = 1
    pathMax = path
    flowMax = 0
    for i in range(nodes):
        if graph[source, i] != 0 and visited[i] == 0:
            if i == destination:
                pathMax.append(i)
                flowMax = min(flow, graph[source, i])
            else:
                new_flow, new_path = depth_first_search(graph, i, destination, min(flow, graph[source, i]), path + [i], visited)
                if new_flow > flowMax:
                    flowMax = new_flow
                    pathMax = new_path
    return flowMax, pathMax
