import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx
import os


def visualizar_scc(grafo, scc_list):
    """
    Visualiza las componentes fuertemente conexas (SCC) de un grafo dirigido usando colores distintos para cada componente.

    Args:
        grafo (GrafoWeb): Una instancia de la clase GrafoWeb que contiene el grafo a visualizar.
        scc_list (list): Una lista de conjuntos, donde cada conjunto representa una componente fuertemente conexa.

    La función asigna un color diferente a cada componente fuertemente conexa y dibuja el grafo utilizando
    un layout de tipo "spring". Los nodos pertenecientes a la misma SCC se pintan del mismo color.
    """
    color_map = []
    colors = cm.get_cmap('hsv', len(scc_list))
    for node in grafo.graph:
        for i, scc in enumerate(scc_list):
            if node in scc:
                color_map.append(colors(i))
                break
    pos = nx.spring_layout(grafo.graph)
    nx.draw(grafo.graph, pos, node_color=color_map, with_labels=True, node_size=50, font_size=8)
    if not os.path.exists('data'):
        os.makedirs('data')
    plt.savefig('data/scc_visualization.png')
    plt.show()