from bs4 import BeautifulSoup
from persistence import *
from utils import *
import logging
import os
import requests


class Crawler:
    """
    Clase para crear un crawler que extrae enlaces de una página web específica.
    Puede navegar a través de enlaces internos hasta una profundidad máxima definida.
    """

    def __init__(self, url_inicio, max_depth=3):
        """
        Inicializa el crawler con la URL de inicio y la profundidad máxima.

        Args:
            url_inicio (str): La URL donde comenzará la búsqueda de enlaces.
            max_depth (int): La profundidad máxima de enlaces a seguir. Por defecto es 3.
        """
        self.url_inicio = url_inicio
        self.urls_visitadas = set()
        self.datos_enlaces = []
        self.max_depth = max_depth

    def obtener(self, url, intentos=3):
        """
        Realiza una solicitud HTTP para obtener el contenido de una URL.

        Args:
            url (str): La URL a la que se desea acceder.
            intentos (int): Cantidad máxima de intentos.

        Returns:
            str: El contenido HTML de la respuesta si la solicitud fue exitosa; de lo contrario, None.
        """
        for _ in range(intentos):
            try:
                respuesta = requests.get(url)
                respuesta.raise_for_status()
                return respuesta.text
            except requests.exceptions.HTTPError as http_err:
                logging.error(f"HTTP error occurred: {http_err} - URL: {url}")
            except requests.exceptions.RequestException as e:
                logging.error(f"Error occurred: {e} - URL: {url}")
            retrasar_solicitud(1)
        return None

    def analizar_enlaces(self, html, url_base, depth):
        """
        Analiza el HTML de una página para extraer enlaces y navega a ellos recursivamente.

        Args:
            html (str): El contenido HTML de la página a analizar.
            url_base (str): La URL base desde donde se están extrayendo los enlaces.
            depth (int): La profundidad actual de la búsqueda.
        """
        sopa = BeautifulSoup(html, 'html.parser')
        for enlace in sopa.find_all('a', href=True):
            href = enlace['href']
            if href.startswith('/') or url_base in href:
                url_completa = requests.compat.urljoin(url_base, href)
                if url_completa not in self.urls_visitadas and 'untref.edu.ar' in url_completa:
                    self.datos_enlaces.append((url_base, url_completa, enlace.text))
                    self.urls_visitadas.add(url_completa)
                    logging.info(f"Crawling: {url_completa}")
                    self.crawl(url_completa, depth + 1)

    def crawl(self, url, depth=0):
        """
        Realiza la operación de crawling para una URL dada, limitado por la profundidad.

        Args:
            url (str): La URL a la que se desea acceder.
            depth (int): La profundidad actual de la búsqueda. Por defecto es 0.
        """
        if depth > self.max_depth:
            return
        html = self.obtener(url)
        if html:
            self.analizar_enlaces(html, url, depth)

    def guardar_enlaces_csv(self, nombre_archivo):
        """
        Guarda los enlaces encontrados en un archivo CSV.
        """
        if not os.path.exists('data'):
            os.makedirs('data')
        headers = ['URL de origen', 'URL de destino', 'Texto del enlace']
        guardar_csv(nombre_archivo, self.datos_enlaces, headers)

    def iniciar(self):
        """
        Inicia el proceso de crawling desde la URL de inicio y guarda los enlaces en un archivo CSV.
        """
        self.crawl(self.url_inicio)
        self.guardar_enlaces_csv('data/links.csv')