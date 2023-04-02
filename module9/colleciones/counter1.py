from collections import Counter

print(Counter('mi perro es un hijo de odin'))

numero = [1,1,1,2,3,4,5,5,6,4,3,2,5,3]
print(Counter(numero))

frase = "ojo por ojo diente por diente y zorra por zorra"
print(Counter(frase.split()))

series = Counter([1,1,1,2,3,4,5,6,5,4,3,4,5,4,3,2,1,3,5,4])
print(series.most_common()) # muestra de mayor a menor lo elementos que se repiten
print(series.most_common(2))#muestra los dos primero con mas repetidos pero si hay iguales lista de menor a mayor
print(list(series))# es una lista sin elemetos repetidos

print(series.items()) #lo trae como una lista ordenada enc ada iterable como tupla
