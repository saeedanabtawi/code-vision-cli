import os
import networkx as nx
import matplotlib.pyplot as plt


def list_to_graph(edges):
    graph = nx.Graph()
    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=float(edge[2]))
    return graph


def build_graph(Graph, Threshold, out_file):
    elarge = [(u, v) for (u, v, d) in Graph.edges(data=True) if d['weight'] > Threshold]
    esmall = [(u, v) for (u, v, d) in Graph.edges(data=True) if d['weight'] <= Threshold]

    # pos=nx.spring_layout(Graph)
    # to give a fixed shape
    pos = nx.spring_layout(Graph, k=0.9, iterations=20)  # positions for all nodes

    nx.draw_networkx_nodes(Graph, pos, node_size=50)
    # edges
    nx.draw_networkx_edges(Graph, pos, edgelist=elarge, width=1)
    nx.draw_networkx_edges(Graph, pos, edgelist=esmall, width=.3, alpha=0.0, edge_color='b', style='dashed')
    # labels
    nx.draw_networkx_labels(Graph, pos, font_size=10, font_family='sans-serif')

    plt.axis('off')
    if os.path.isfile(out_file):
        os.remove(out_file)
    else:
        plt.savefig(out_file)  # save as png

    # plt.show() # display

    return None
