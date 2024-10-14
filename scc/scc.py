import csv
import networkx as nx


class SCC:

    def __init__(self, grafo):
        self.grafo = grafo

    def calcular_scc(self):
        return list(nx.strongly_connected_components(self.grafo.graph))

    def guardar_resultados(self, file_name):
        scc_list = self.calcular_scc()
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['SCC ID', 'URLs'])
            for i, scc in enumerate(scc_list):
                # Cada componente fuertemente conexa (SCC) se representa como una lista de URLs
                writer.writerow([i, ", ".join(scc)])  # i es el ID del SCC, list(scc) son las URLs