from persistence import *
from utils import es_url_valida
import logging
import networkx as nx


class GrafoWeb:
    """
    Clase para representar un grafo dirigido que modela la relación entre URLs.
    Utiliza la biblioteca NetworkX para manejar la estructura del grafo.
    """

    def __init__(self):
        """
        Inicializa un nuevo grafo dirigido.
        """
        self.graph = nx.DiGraph()

    def agregar_nodo(self, url):
        """
        Agrega un nodo al grafo para la URL especificada.

        Args:
            url (str): La URL que se desea agregar como nodo.
        """
        self.graph.add_node(url)

    def agregar_arista(self, origen, destino):
        """
        Agrega una arista dirigida entre dos nodos (URLs) en el grafo.

        Args:
            origen (str): La URL de origen.
            destino (str): La URL de destino.

        Raises:
            Warning: Si alguna de las URLs no es válida, se registrará una advertencia en el log.
        """
        if es_url_valida(origen) and es_url_valida(destino):
            self.graph.add_edge(origen, destino)
        else:
            logging.warning(f"Invalid URLs: {origen} -> {destino}")

    def construir_desde_csv(self, file_name):
        """
        Construye el grafo a partir de un archivo CSV que contiene relaciones de URLs.

        Args:
            file_name (str): El nombre del archivo CSV de entrada. Se espera que el archivo tenga
                             tres columnas: origen, destino y texto del enlace (este último se ignora).

        Raises:
            Warning: Si una línea no tiene suficientes valores o se encuentra con URLs no válidas.
            Error: Si ocurre un error al procesar una línea específica.
        """
        try:
            rows = cargar_csv(file_name)
            for line_number, parts in enumerate(rows[1:], start=2):
                if len(parts) < 3:
                    logging.warning(f"Línea ignorada (no tiene suficientes valores): {parts}")
                    continue
                try:
                    origen, destino, _ = parts
                    self.agregar_nodo(origen)
                    self.agregar_nodo(destino)
                    self.agregar_arista(origen, destino)
                except ValueError as e:
                    logging.error(f"Error en la línea {line_number}: {parts} - {e}")
        except Exception as e:
            logging.error(f"Error al cargar el archivo CSV: {e}")

    def guardar_en_archivo(self, file_name):
        """
        Guarda la representación del grafo en un archivo en formato de lista de adyacencia.

        Args:
            file_name (str): El nombre del archivo donde se guardará el grafo.
        """
        nx.write_adjlist(self.graph, file_name)