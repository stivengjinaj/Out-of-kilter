import networkx as nx
from matplotlib import pyplot as plt


def plot_graph(visual_graph):
    edges = [(u, v) for (u, v, d) in visual_graph.edges(data=True)]

    num_nodes = visual_graph.nodes
    node_pos = {}
    pos_x = 1
    pos_y = 2
    i = 1

    while i <= len(num_nodes):
        if i % 2 != 0:
            node_pos[i] = (pos_x, pos_y)
        else:
            if i == 1:
                node_pos[i] = (pos_x, pos_y+1)
            else:
                if i == len(num_nodes):
                    node_pos[i] = (pos_x, pos_y)
                    break
                else:
                    node_pos[i] = (pos_x, pos_y+1)
                    i += 1
                    node_pos[i] = (pos_x, pos_y-1)
        i += 1
        pos_x += 1

    # nodes
    nx.draw_networkx_nodes(visual_graph, node_pos, node_size=700)

    # node labels
    nx.draw_networkx_labels(visual_graph, node_pos, font_size=10, font_family="sans-serif")

    # edges
    nx.draw_networkx_edges(visual_graph, node_pos, edgelist=edges, width=3, alpha=0.5, edge_color="b")

    # Combine edge attributes into a single dictionary
    edge_labels = {}
    edge_uppers = nx.get_edge_attributes(visual_graph, "upper")
    edge_costs = nx.get_edge_attributes(visual_graph, "cost")
    for edge in edges:
        edge_labels[edge] = f"({edge_costs[edge]}, {edge_uppers[edge]})"


    # Display edge labels
    nx.draw_networkx_edge_labels(visual_graph, node_pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.05)
    plt.axis("off")
    plt.title("INITIAL GRAPH (cost, capacity)\n")
    plt.show()
