lista_numeros =[-45,56,23,15,85,1000]
def suma_menores(numeros):
    contador = 0
    for numero in numeros:
        if 0<numero and numero<1000:
            contador += numero
    return contador