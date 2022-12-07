###comprhensions, dictionary comprhensions, map, filter, modules
# Gamee de piedra papal o tijera
# lambda(funciones anonimas)



# numbers =[element for element in range(1,11)]
# print(numbers)

# numbers_x2 =[element*2 for element in range(1,11)]
# print(numbers_x2)

# numbers_mod2 =[element**2 for element in range(1,11) if element % 2 ==0]
# print(numbers_mod2)


##normal
# dicti = {}
# for i in range(1,11):
#     dicti[i] = i*5
# print(dicti)

# #dict comprhensions
# dicti ={element:element**2 for element in range(1,11)}
# print(dicti)


# import random
# countries = ['col','mex','arg','per']
# population = {country :random.randint(100000,999999) for country in countries}
# print(population)


# names = ['nicolas','brandon','mabel']
# ages = [23,26,21]
# print(list(zip(names,ages)))

# dicti = {name : age for (name,age) in zip (names,ages)}
# print(dicti)



# import random
# countries = ['col','mex','arg','per']
# population = {country :random.randint(100000,999999) for country in countries}
# print(population)

# population_high = {country : population2
# for (country, population2) in population.items() if population2 > 500000}
# print(population_high)

# txt = "Hola hijos de odin"
# unique = {o: o.upper() for o in txt if o in 'aeiou'}
# print(unique)




##funciones de orden superior
# def suma(num):
#     return num*3

# ##la funciones que resivenuna funcion solo se escribe y no se hace el llamado () ya que seria un error solo necesita el nombre
# def suma_superior(num,func):
#     return num + func(num)
# ##operacion 4 + (4 * 3)
# print(suma_superior(4,suma))



# ##hay que tener cuidado por que se modifica el orginal por que se comparte la misma referencia en memoria
# def add_taxes(item):
#     new_item = item.copy()
#     new_item['Iva'] = new_item['precio'] * .19
#     return new_item

# new_items = list(map(add_taxes, items))
# print(new_items)
# print(items)




# import functools
# numbers = [3,1,2,4]
# result = functools.reduce(lambda contador, item: contador + item, numbers)
# result = sum(numbers)
# print(result)


###modules
##para saber la ruta donde se ejecuta
# import sys
# print(sys.path)

##para encontrar los numeros en un texto
# import re
# text = 'Perro smi numero es 310 415 2563 y el code del pais es 57, pero ma mi gusta el numero 7'
# print(re.findall('[0-9]+',text))

# import time
# print(time.localtime())
# print(time.asctime())

# #colletions
# import collections
# numbers = [1,1,4,5,8,2,3,5,9,4,2]
# print(collections.Counter(numbers))


###manejo de errores
try:
    print(0/0)
except ZeroDivisionError as error:
    print("que man tan bobo dividiendo por 0")