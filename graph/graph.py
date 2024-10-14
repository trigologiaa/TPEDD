from utils import es_url_valida
import logging
import networkx as nx


class GrafoWeb:

    def __init__(self):
        self.graph = nx.DiGraph()

    def agregar_nodo(self, url):
        self.graph.add_node(url)

    def agregar_arista(self, origen, destino):
        if es_url_valida(origen) and es_url_valida(destino):
            self.graph.add_edge(origen, destino)
        else:
            logging.warning(f"Invalid URLs: {origen} -> {destino}")

    def construir_desde_csv(self, file_name):
        with open(file_name, 'r') as file:
            for line_number, line in enumerate(file.readlines()[1:], start=2):
                stripped_line = line.strip()
                if not stripped_line:
                    continue
                parts = stripped_line.split(',')
                if len(parts) < 3:
                    logging.warning(f"Línea ignorada (no tiene suficientes valores): {stripped_line}")
                    continue
                try:
                    origen, destino, _ = parts
                    self.agregar_nodo(origen)
                    self.agregar_nodo(destino)
                    self.agregar_arista(origen, destino)
                except ValueError as e:
                    logging.error(f"Error en la línea {line_number}: {stripped_line} - {e}")

    def guardar_en_archivo(self, file_name):
        nx.write_adjlist(self.graph, file_name)