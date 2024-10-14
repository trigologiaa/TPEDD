import matplotlib.pyplot as plt


def visualizar_pagerank(resultados):
    sorted_results = sorted(resultados.items(), key=lambda x: x[1], reverse=True)[:10]
    urls, ranks = zip(*sorted_results)
    plt.barh(urls, ranks)
    plt.xlabel('PageRank')
    plt.ylabel('URL')
    plt.title('Top 10 PageRank')
    plt.show()