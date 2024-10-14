import csv


def guardar_csv(file_name, data, headers=None):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        if headers:
            writer.writerow(headers)
        writer.writerows(data)

def cargar_csv(file_name):
    with open(file_name, 'r') as file:
        return list(csv.reader(file))