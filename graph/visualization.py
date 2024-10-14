import networkx as nx
import matplotlib.pyplot as plt

def visualizar_grafo(grafo):
    posicion = nx.spring_layout(grafo.graph)
    plt.figure(figsize=(10, 8))
    nx.draw(grafo.graph, posicion, with_labels=True, node_size=50, font_size=8, arrows=True)
    plt.savefig('data/grafo.png')
    plt.show()