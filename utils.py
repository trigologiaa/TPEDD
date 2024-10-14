from time import sleep
import requests


def retrasar_solicitud(segundos):
    sleep(segundos)

def es_url_valida(url):
    try:
        respuesta = requests.head(url)
        return respuesta.status_code == 200
    except Exception:
        return False