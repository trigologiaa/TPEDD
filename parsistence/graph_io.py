import networkx as nx


def guardar_grafo(grafo, file_name):
    nx.write_adjlist(grafo.graph, file_name)

def cargar_grafo(file_name):
    grafo = nx.read_adjlist(file_name, create_using=nx.DiGraph())
    return grafo