import matplotlib.pyplot as plt
import networkx as nx


def visualizar_scc(grafo, scc_list):
    color_map = []
    for node in grafo.graph:
        for i, scc in enumerate(scc_list):
            if node in scc:
                color_map.append(i)
                break
    pos = nx.spring_layout(grafo.graph)
    nx.draw(grafo.graph, pos, node_color=color_map, with_labels=True, node_size=50, font_size=8)
    plt.show()