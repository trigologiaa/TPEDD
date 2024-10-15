import logging
import networkx as nx


def guardar_grafo(grafo, file_name):
    """
    Guarda un grafo en un archivo en formato de lista de adyacencia.

    Args:
        grafo (GrafoWeb): Una instancia de la clase GrafoWeb que contiene el grafo a guardar.
        file_name (str): El nombre del archivo donde se guardará el grafo.

    Esta función utiliza la biblioteca NetworkX para escribir la representación del grafo en un archivo
    usando el formato de lista de adyacencia.
    """
    nx.write_adjlist(grafo.graph, file_name)

def cargar_grafo(file_name):
    """
    Carga un grafo desde un archivo en formato de lista de adyacencia.

    Args:
        file_name (str): El nombre del archivo desde el cual se cargará el grafo.

    Returns:
        DiGraph: Un objeto DiGraph de NetworkX que representa el grafo cargado.

    Esta función utiliza la biblioteca NetworkX para leer la representación del grafo desde un archivo
    y devuelve un grafo dirigido.
    """
    try:
        grafo = nx.read_adjlist(file_name, create_using=nx.DiGraph())
        return grafo
    except Exception as e:
        logging.error(f"Error al cargar el grafo desde el archivo: {e}")
        return nx.DiGraph()