import csv
import logging


def guardar_csv(file_name, data, headers=None):
    """
    Guarda datos en un archivo CSV.

    Args:
        file_name (str): El nombre del archivo CSV donde se guardarán los datos.
        data (list of lists): Los datos a guardar, donde cada sublista representa una fila en el CSV.
        headers (list, optional): Una lista de encabezados para las columnas. Si se proporciona, se escribirá como la primera fila del archivo.

    Esta función abre el archivo en modo escritura y guarda los datos en formato CSV. 
    Si se proporcionan encabezados, estos se escriben como la primera fila.
    """
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if headers:
                writer.writerow(headers)
            writer.writerows(data)
    except IOError as e:
        logging.error(f"Error al guardar el archivo CSV: {e}")

def cargar_csv(file_name):
    """
    Carga datos desde un archivo CSV.

    Args:
        file_name (str): El nombre del archivo CSV desde el cual se cargarán los datos.

    Returns:
        list of lists: Una lista de filas leídas del archivo CSV, donde cada fila es una lista de valores.

    Esta función abre el archivo en modo lectura y devuelve el contenido como una lista de listas.
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return list(csv.reader(file))
    except IOError as e:
        logging.error(f"Error al cargar el archivo CSV: {e}")
        return []