lista_numeros = [1,2,15,7,2,8]

import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        return []
    elif moneda == "Cruz":
        print("La lista fue salvada")
        return lista