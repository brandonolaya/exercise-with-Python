lista_numeros = [1,50,502,5000,755,600,33,61]

def cantidad_pares(lista_numeros):
    cantidad=0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad += 1
    return cantidad