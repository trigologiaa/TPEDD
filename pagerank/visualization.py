import matplotlib.pyplot as plt
import os


def visualizar_pagerank(resultados, top_n=10):
    """
    Visualiza los resultados del algoritmo PageRank en un gráfico de barras horizontal.

    Args:
        resultados (dict): Un diccionario donde las claves son URLs y los valores son los puntajes de PageRank.
        top_n (int): Número de URLs a mostrar en la visualización. Por defecto es 10.
        
    La función ordena los resultados de PageRank y selecciona las top_n URLs con mayor puntaje.
    Luego, genera un gráfico de barras horizontal mostrando el PageRank de estas URLs.
    """
    sorted_results = sorted(resultados.items(), key=lambda x: x[1], reverse=True)[:top_n]
    urls, ranks = zip(*sorted_results)
    plt.barh(urls, ranks)
    plt.xlabel('PageRank')
    plt.ylabel('URL')
    plt.title(f'Top {top_n} PageRank')
    if not os.path.exists('data'):
        os.makedirs('data')
    plt.savefig('data/pagerank_visualization.png')
    plt.show()