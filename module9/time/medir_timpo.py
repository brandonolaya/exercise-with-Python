import time
import timeit

# def test_for(numero):
#     lista= []
#     for i in range(1,numero+1):
#         lista.append(i)
#     return(lista)


# def test_while(numeros):
#     lista = []
#     contador = 1
#     while contador <= numeros:
#         lista.append(contador)
#         contador += 1
#     return lista

# se usa con el modulo time
# inicio = time.time()
# test_for(1500)
# final = time.time()
# print(final - inicio)

# inicio = time.time()
# test_while(1500)
# final = time.time()
# print(final - inicio)

declaracion = """
test_for(15)
"""

stup = """
def test_for(numero):
    lista= []
    for i in range(1,numero+1):
        lista.append(i)
    return(lista)
"""
duracion = timeit.timeit(declaracion, stup, number=1000000)
print(duracion)

declaracion2 = """
test_while(15)
"""

stup2 = """
def test_while(numeros):
    lista = []
    contador = 1
    while contador <= numeros:
        lista.append(contador)
        contador += 1
    return lista
"""

duracion2 = timeit.timeit(declaracion2, stup2, number=1000000)
print(duracion2)

