from bs4 import BeautifulSoup
import csv
import logging
import requests


class Crawler:

    def __init__(self, url_inicio, max_depth=3):
        self.url_inicio = url_inicio
        self.urls_visitadas = set()
        self.datos_enlaces = []
        self.max_depth = max_depth

    def obtener(self, url):
        try:
            respuesta = requests.get(url)
            respuesta.raise_for_status()
            return respuesta.text
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err} - URL: {url}")
        except requests.exceptions.ConnectionError as conn_err:
            logging.error(f"Connection error occurred: {conn_err} - URL: {url}")
        except requests.exceptions.Timeout:
            logging.error(f"Timeout error: {url}")
        except requests.exceptions.TooManyRedirects:
            logging.error(f"Too many redirects: {url}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e} - URL: {url}")
        return None

    def analizar_enlaces(self, html, url_base, depth):
        sopa = BeautifulSoup(html, 'html.parser')
        for enlace in sopa.find_all('a', href=True):
            href = enlace['href']
            if href.startswith('/') or url_base in href:
                url_completa = requests.compat.urljoin(url_base, href)
                if url_completa not in self.urls_visitadas and 'untref.edu.ar' in url_completa:
                    self.datos_enlaces.append((url_base, url_completa, enlace.text))
                    self.urls_visitadas.add(url_completa)
                    self.crawl(url_completa, depth + 1)

    def crawl(self, url, depth=0):
        if depth > self.max_depth:
            return
        html = self.obtener(url)
        if html:
            self.analizar_enlaces(html, url, depth)

    def guardar_enlaces_csv(self, nombre_archivo):
        try:
            with open(nombre_archivo, mode='w', newline='') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(['URL de origen', 'URL de destino', 'Texto del enlace'])
                for fila in self.datos_enlaces:
                    escritor.writerow(fila)
        except IOError as e:
            logging.error(f"Error al guardar el archivo CSV: {e}")
        except Exception as e:
            logging.error(f"Error inesperado al guardar CSV: {e}")

    def iniciar(self):
        self.crawl(self.url_inicio)
        self.guardar_enlaces_csv('data/links.csv')