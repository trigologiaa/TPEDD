from persistence import *
import networkx as nx


class SCC:
    """
    Clase para calcular y almacenar las componentes fuertemente conexas (SCC) de un grafo dirigido.

    Attributes:
        grafo (GrafoWeb): Una instancia de la clase GrafoWeb que representa el grafo a analizar.
    """

    def __init__(self, grafo):
        """
        Inicializa la clase SCC con un grafo dado.

        Args:
            grafo (GrafoWeb): Una instancia de la clase GrafoWeb que se utilizará para el cálculo de SCC.
        """
        self.grafo = grafo

    def calcular_scc(self):
        """
        Calcula las componentes fuertemente conexas del grafo.

        Returns:
            list: Una lista de conjuntos, donde cada conjunto contiene las URLs que forman una componente fuertemente conexa.
        """
        return list(nx.strongly_connected_components(self.grafo.graph))

    def guardar_resultados(self, file_name):
        """
        Guarda los resultados de las componentes fuertemente conexas en un archivo CSV.
        """
        try:
            scc_list = self.calcular_scc()
            data = [(i, ", ".join(scc)) for i, scc in enumerate(scc_list)]
            headers = ['SCC ID', 'URLs']
            guardar_csv(file_name, data, headers)
        except Exception as e:
            logging.error(f"Error al guardar los resultados de SCC: {e}")