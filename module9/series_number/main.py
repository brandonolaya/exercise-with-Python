import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()
ruta = 'module9/series_number/Mi_Gran_Directorio'
patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
num_encontrado = []
archivo_encontrado = []


def buscar_numero(archivo, patron):
    """
    Busca dentro del los archivos patrones que coincidan
    """
    this_archivo = open(archivo, 'r')
    texto = this_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return '' #para evitar que se llene de None


def crear_lista():
    """
    almecena los numero concontrados en una lista cuando recorre el arbol
    """
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), patron)
            if resultado != '':
                num_encontrado.append(resultado.group())
                archivo_encontrado.append(a.title())


def mostrar():
    indice = 0
    print('-' * 50)
    print(f'Fecha Consulta: {hoy.day}/{hoy.month}/{hoy.year}\n')
    print('Archivo \t\tNRO. SERIE')
    print('-------\t\t\t----------')

    for a in archivo_encontrado:
        print(f'{a}\t\t{num_encontrado[indice]}')
        indice += 1

    print('\n')
    print(f'Numeros encontrado: {len(num_encontrado)}')
    final = time.time()
    duracion = final - inicio
    print(f'Duracion Buscqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


if __name__ == "__main__":
    crear_lista()
    mostrar()
