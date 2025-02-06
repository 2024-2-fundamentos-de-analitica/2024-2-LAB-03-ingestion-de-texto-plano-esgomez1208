"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    with open('files/input/clusters_report.txt', 'r') as file:
        lineas = file.readlines()

    data = []
    cluster = None
    for linea in lineas[4:]:
        if linea.strip():
            partes = linea.split()
            if partes[0].isdigit():
                if cluster:
                    data.append(cluster)
                cluster = int(partes[0])
                num_palabras_clave = int(partes[1])
                porcentaje_palabras_clave = float(partes[2].replace(',', '.').replace('%', ''))
                palabras_clave_principales = ' '.join(partes[3:])
                cluster = {
                    'cluster': cluster,
                    'cantidad_de_palabras_clave': num_palabras_clave,
                    'porcentaje_de_palabras_clave': porcentaje_palabras_clave,
                    'principales_palabras_clave': palabras_clave_principales
                }
            else:
                cluster['principales_palabras_clave'] += ' ' + ' '.join(partes)

    if cluster:
        data.append(cluster)
    df = pd.DataFrame(data)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace(' ,', ',').str.replace(', ', ', ').str.replace('  ', ' ').str.strip('.').str.lstrip('% ')
    return df
