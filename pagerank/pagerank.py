import csv
import networkx as nx


class PageRank:

    def __init__(self, grafo):
        self.grafo = grafo
        self.results = {}

    def calcular(self, damping_factor=0.85, max_iter=100):
        self.results = nx.pagerank(self.grafo.graph, alpha=damping_factor, max_iter=max_iter)

    def guardar_resultados(self, file_name):
        with open(file_name, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['URL', 'PageRank'])
            for url, rank in self.results.items():
                writer.writerow([url, rank])