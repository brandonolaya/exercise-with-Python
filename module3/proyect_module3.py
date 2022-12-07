###using the slices, asto access a specific position,
# search using index, split, join, replace, reverse, sort,len,pop,append,set,add,clear,booleans
# diccionaries, nested dictionaries, tuples
# last exercise text analysis


# mi_texto = "Soy una prueba"
# resultado = mi_texto[-6]


# no infiere entre mayusculas i minusculas
# resultado = mi_texto.index("U")


# desde donde inicia la busqeuda
# resultado = mi_texto.index("u",5)


# tamaño determinado para la busqueda
# resultado = mi_texto.index("u",4,11)


# busqeuda invertida
# resultado = mi_texto.rindex("u")



# Buscar una palabra
# mi_texto = "hijo de puta Hola"
# print("hola" in mi_texto)
# print(len(mi_texto))


# print(15*"Repetición")
# print("agua" not in "Tierra mojada mis recuerdos de viaje, entre las lluvias")
# print(len('electroencefalografista'))


# listas
# mi_lista = ['a','b','c']
# mi_lista2 = [1,2,3]
# mi_lista2.append('4')
# mi_lista.pop(1)
# print(mi_lista + mi_lista2)





# lista ordenada
# mi_lista = [5,6,9,1,2,7]
# mi_lista2 = ['n','g','l','i','a','h']
# sort,reverse realiza una accion pero no lo asigna a nada asi que no se puede almacenar
# mi_lista2.sort()
# mi_lista.reverse()
# print(mi_lista2)


# mi_lista = [1,2,3,4,5]

# medios_transporte = ["avión", "auto", "barco", "bicicleta"]
# medios_transporte.append("motocicleta")

# frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
# eliminado = frutas[2]
# frutas.pop(2)
# print(eliminado)


# Diccionarios estos no se pueden buscar por indices sino por claves
# diccionario = {'clave1':"valor1",
#                'clave2':'valor2'
#                }
# print(diccionario["clave2"])

# dic = {
#    'c1':10,
#    'c2':[15,20,25],
#    'c3':{
#        's1':100,
#       's2':200,
#       },
#    'c4':{
#        'k1':'a',
#        'k2':'b',
#    },
#    nombre : 'brandon'
# }
# print(dic['c4']['k2'].upper())
# dic['c5'] = 'brandon'
# print(dic)

# mi_dic = {
#     'nombre': 'Karen',
#     'apellido': 'Jurgens',
#     'edad': 35,
#     'ocupacion': 'Periodista',
#     }




#########################################################
#tuplas son inmutables
#mi_tuple= 1,2,3,4,5,6
#print(mi_tuple[-0])
#tuple =(1,2,1,3,4,1,3)
#x,y,z = tuple #debe tener los mismos elementos
#print(tuple.count(1))
#print(tuple.index(4))



#los sets, no tiene indices, no tiene elementos repetidos, no se pueden incluir listas o diccionarios,
# pero si admite tuples por que son inmutables
#el set se identifica con el parentesis y por dentro puedo cambiarlo
# mi_set = set(('a','b','c','d','a','b','c','d','e'))
# mi_set2 = set({'a','b','c','d','a','b','c','d','e','f'})
# mi_set3 = set(['a','b','c','d','a','b','c','d','e',4,3])
# print(len(mi_set))
# print ('2' in mi_set3)



#la funcion add no agrega algo que ya esta igual
#remove quita algun elemento pero si este no esta da erro
#discar lo mismo pero no da error
#pop quitara el primer elemento en los sets si son numeros
# s1 = {1,2,3}
# s1.add(4)
# s1.discard(2)
# sorteo = s1.pop()
# s1.clear()
# print(sorteo)




####conjuntos se identifican con {}
# set_conuntries = {'col','mex','bol'}
# size = len(set_conuntries)
# print(size)
# print('col' in set_conuntries)
# print('per' in set_conuntries)
# set_conuntries.add('jap')
# print('jap' in set_conuntries)

# set_conuntries.update({'kor','arg'})
# print(set_conuntries)

# ##remove da error si no lo encueuntra
# set_conuntries.remove('kor')
# set_conuntries.discard('kor')
# print(set_conuntries)



#####Operar conjuntos
# set_city1 = {'bog','med','iba'}
# set_city2 = {'bar','tun','med'}
# set_citys = set_city1.union(set_city2)
# print(set_citys)
# ##operador matematico para unirlos
# print(set_city1 | set_city2)

# ##intersection
# set_unico = set_city1.intersection(set_city2)
# print(set_unico)
# #operador
# print(set_city1 & set_city2)

# ###differencia solo deja elementos del primer conjunto elegido
# set_difference = set_city1.difference(set_city2)
# print(set_difference)
# ##operador
# print(set_city2 - set_city1)


# ###diferencia symetrica que es apartando las en comun
# set_simetric = set_city1.symmetric_difference(set_city2)
# print(set_simetric)
# ##operador
# print(set_city1 ^ set_city2)


#valores booleanos
# > mayor que
# <menor que
# => mayor o igual que
# <= menos o igual queue
# == igual que
# != diferente que




# hacer un programa que cuentre cuantas veces aparece tres letras determinada en una lista
# contar el total de palabra en total
# cual es la primera y ultima letra del texto
# invertir el tecto
texto = input("Escribe un texto : ").upper()
lista_palabra= []
lista_palabra.append(input("Primera letra: ").upper())
lista_palabra.append(input("Legunda letra: ").upper())
lista_palabra.append(input("Tercera letra: ").upper())

palabras_texto = texto.split()

primera_letra = palabras_texto[0]
ultima_letra = palabras_texto[-1]

palabras_texto.reverse()
texto_invertido = ' '.join(palabras_texto)

buscar_python = 'PYTHON' in texto
dic = {
    True:"si",
    False:"no"
}

print('\nCANTIDAD DE LETRAS')
print(F'Se encontraron "{texto.count(lista_palabra[0])}" de la letra "{lista_palabra[0]}"')
print(F'Se encontraron "{texto.count(lista_palabra[1])}" de la letra "{lista_palabra[1]}"')
print(F'Se encontraron "{texto.count(lista_palabra[2])}" de la letra "{lista_palabra[2]}"\n')

print("\nCANTIDAD DE PALABRAS")
print(f'En el texto hay "{len(palabras_texto)}" de palabras\n')

print("\nLETRA DE INICIO Y FIN")
print("la primera letra es: \t",primera_letra[0])
print("la ultima letra es: \t",ultima_letra[-1])

print("\nTEXTO INVERTIDO")
print(f'{texto_invertido}\n')

print("\nBUSCANDO LA PALABRA PYTHON")
print(f'La palabra "Python" {dic[buscar_python]} se encuentra en el texto')
