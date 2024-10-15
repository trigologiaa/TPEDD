from persistence import *
import networkx as nx


class PageRank:
    """
    Clase para calcular y almacenar el algoritmo PageRank sobre un grafo dirigido.

    Attributes:
        grafo (GrafoWeb): Una instancia de la clase GrafoWeb que representa el grafo sobre el cual se calculará el PageRank.
        results (dict): Un diccionario que almacenará los resultados del PageRank, donde las claves son URLs y los valores son los puntajes de PageRank.
    """

    def __init__(self, grafo):
        """
        Inicializa la clase PageRank con un grafo dado.

        Args:
            grafo (GrafoWeb): Una instancia de la clase GrafoWeb que se utilizará para el cálculo del PageRank.
        """
        self.grafo = grafo
        self.results = {}

    def calcular(self, damping_factor=0.85, max_iter=100):
        """
        Calcula el PageRank de las URLs en el grafo utilizando el algoritmo de PageRank de NetworkX.

        Args:
            damping_factor (float): Factor de amortiguación que controla la probabilidad de seguir enlaces. Por defecto es 0.85.
            max_iter (int): Número máximo de iteraciones para el algoritmo. Por defecto es 100.
        """
        self.results = nx.pagerank(self.grafo.graph, alpha=damping_factor, max_iter=max_iter)

    def guardar_resultados(self, file_name):
        """
        Guarda los resultados del cálculo de PageRank en un archivo CSV.
        """
        try:
            data = [(url, rank) for url, rank in self.results.items()]
            headers = ['URL', 'PageRank']
            guardar_csv(file_name, data, headers)
        except Exception as e:
            logging.error(f"Error al guardar los resultados: {e}")