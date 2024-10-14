import logging
import matplotlib
matplotlib.use('Qt5Agg')
from crawler.crawler import Crawler
from graph.graph import GrafoWeb
from graph.visualization import visualizar_grafo
from pagerank.pagerank import PageRank
from pagerank.results import visualizar_pagerank
from scc.scc import SCC
from scc.visualization import visualizar_scc


logging.basicConfig(filename='data/crawler.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    logging.info("Iniciando el crawler...")
    try:
        crawler = Crawler('https://www.untref.edu.ar')
        crawler.iniciar()
        logging.info("Crawler completado con éxito.")
        grafo_web = GrafoWeb()
        grafo_web.construir_desde_csv('data/links.csv')
        logging.info("Grafo construido desde CSV con éxito.")
        visualizar_grafo(grafo_web)
        pagerank = PageRank(grafo_web)
        pagerank.calcular()
        pagerank.guardar_resultados('data/pagerank_results.csv')
        logging.info("Resultados de PageRank guardados con éxito.")
        visualizar_pagerank(pagerank.results)
        scc = SCC(grafo_web)
        scc_list = scc.calcular_scc()
        scc.guardar_resultados('data/scc_results.csv')
        logging.info("Resultados de SCC guardados con éxito.")
        visualizar_scc(grafo_web, scc_list)
    except KeyboardInterrupt:
        logging.warning("Se terminó la ejecución del programa antes de finalizar.")
    except Exception as e:
        logging.error(f"Error durante la ejecución del programa: {e}")
    logging.info("Programa terminado.")