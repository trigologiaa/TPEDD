import matplotlib.pyplot as plt
import networkx as nx
import os

def visualizar_grafo(grafo):
    """
    Visualiza un grafo dirigido utilizando la biblioteca Matplotlib.

    Args:
        grafo (GrafoWeb): Una instancia de la clase GrafoWeb que contiene el grafo a visualizar.

    El grafo se dibuja utilizando un layout de tipo "spring", que distribuye los nodos de forma que
    se minimicen las aristas cruzadas. La visualización se guarda en un archivo PNG y se muestra en
    pantalla.

    Raises:
        ValueError: Si el objeto pasado no es una instancia de GrafoWeb.
    """
    if not os.path.exists('data'):
        os.makedirs('data')
    posicion = nx.spring_layout(grafo.graph)
    plt.figure(figsize=(10, 8))
    nx.draw(grafo.graph, posicion, with_labels=True, node_size=50, font_size=8, arrows=True)
    plt.savefig('data/grafo.png')
    plt.show()