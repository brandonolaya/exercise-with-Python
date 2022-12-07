#### boolean, not in text or list, if-elif-else, match loop while,for,
# startswith, range, enumerate, zip, min,max,round,  sum, mix,importar, Comprehensions
# ramdon randint, choice, uniform, shuffle,random
# last exercise guess a number using boolean, to indicate whether the numer is greater or less



################################################
#serie = 'C-04'

# if serie == 'C-01':
#     print('te salvaste')
# elif serie == 'C-02':
#     print('corre perra')
# elif serie == 'C-04':
#     print('Te moriste')
# else:
#     print('falsa alarma')

# serie = 'C-04'
# match serie:
#     case 'C-01':
#         print('te salvaste')
#     case 'C-02':
#         print('corre perra')
#     case 'C-04':
#         print('Te moriste')
#     case _:
#         print('falsa alarma')




###########################################################################
###Loop /for


# lista = ['A','B','C','D','E']
# for indice in lista:
#     numero_letra = lista.index(indice) + 1
#     print(f'Letra {numero_letra}: {indice}')


# #busca los que inician con la letra indicada
# lista_nombres = ['pablo', 'julia', 'lucho', 'laura', 'angela']
# for nombre in lista_nombres:
#     if nombre.startswith('l'):
#         print(nombre)





#######################################################################
##loop while
# monedas = 5

# while monedas > 0:
#     print(f'Tengo {monedas} monedas')
#     monedas = monedas - 1

# mun1 = 1

# while mun1 == 1:
#     pass # es como para dejar un espacio reservado para codigo
# print("perros")


# nombre = input("Tu nombre: ")
# for i in nombre:
#     if i == 'n':
#         continue
#     else:
#         print(i)


# lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

# for numero in lista_numeros:
#     if numero >= 0:
#         print(numero)
#     else:
#         break



####################################################################################
#Rangos (range) crea un rango de numero sin necesidad de crar una lista o variable

# for numero in range(2,21,2):
#     print(numero)

# mi_lista = []
# for numero in range(3,301,3):
#     mi_lista.append(numero)
# print(mi_lista)

# suma_cuadrados = 0
# for numero in range(1,16):
#     suma_cuadrados += numero**2
# print(suma_cuadrados)


######################################################################
#enumerado (enumerate) ayuda a acceder facilmente a los indices

# lista = ['a','b','c','d']
# indice = 0
# for item in lista:
#     print(indice,item)
#     indice += 1

# for item in enumerate(lista):
#     print(item)

# for indice,item in enumerate(lista):
#     print(indice, item)

# for indice,item in enumerate(range(25,36)):
#     print(indice, item)

# mis_tuples = list(enumerate(lista))
# print(mis_tuples)
# print(mis_tuples[1][-3])



###################################################################
##el zip llega hasta el largo de la list mas corta
# nombres = ['Brandon', 'Daniel', 'Yuli']
# edades = [26,24,25, 56,34]
# apellido = ['Olaya','Mejia', 'Ganlindez']

# #mezcla = zip(nombres,edades,apellidos)
# mezcla = list(zip(nombres,edades,apellido))
# print(mezcla)

# for nombre,edad,apellido in mezcla:
#     print(f'{nombre} tiene {edad} años y su apellido es {apellido}')


#####################################################################
##min y max

# lista =  [45, 55, 80,12 , 9,35]
# lista2 =  max(45, 55, 80,12 ,35)
# print(min(lista),lista2)

# nombres = ['BRandon', 'Alicia', 'Fernando']
# print(f'el primer nombre es {min(nombres)} y el ultimo nombre es {max(nombres)}')

# nombre = 'BrAndon'
# print(min(nombre),max(nombre))


# dic = {
#     'C1': 45, 'C2':12
#     }
# print(min(dic.values()))






######################################################################################
#importar libreria para el ramdom, tiene aplicacion en juegos o cosas alazar

# from random import randint, random

# aletario = randint(1,100)
# print(aletario)

# from random import *

# aleatorio = uniform(1,5)
# print(aleatorio)

# aleatorio = uniform(1,30)
# print(aleatorio)

# aleatorio = round( uniform(1,54),2)
# print(aleatorio)


# aleatorio = random()
# print(aleatorio)

# colores = ['azul','rojo', 'verde','negro']
# alatorio = choice(colores)
# print(alatorio)

# numeros = list(range(0,101,5))
# shuffle(numeros)
# print(numeros)



#######################################################################
#compresion o modo eficiente menor uso de codigo para contriir algo

# palabra = 'python'
# lista = []
# for letra in palabra:
#     lista.append(letra)
# print(lista)

# lista = [letricas for letricas in palabra]
# lista2 = [letricas for letricas in 'palabra']
# print(lista)
# print(lista2)
# lista_numero = [n/3 for n in range(-30,61,3)]
# print(lista_numero)

# lista_numero2 = [n for n in range(-30,61,3) if n * 2 >10]
# print(lista_numero2)

#lista_numero2 = [n for n in range(-30,61,3) if n * 2 >10 else 'no']# no funcionara con el else debe ir en otro lado
# lista_numero2 = [n if n * 2 >10 else 'no' for n in range(-30,61,3) ]
# print(lista_numero2)


# centimetros = [5000,4500,96050,412]
# metros = [c / 100 for c in centimetros]
# print(metros)




# cliente = {
#     'nombre':'Brandon',
#     'edad': 26,
#     'ocupacion' : 'profesor',
#     }
# comida = {
#     'hamburguesa':"de pollo apanado",
#     'ingredientes':{
#         'pan':'oregano',
#         'carne':'pollo',
#         'salsa':'BBQ chili'
#         }
#     }

# elementos = [cliente, comida, 'gaseosa']

# for e in elementos:
#     match e:
#         case {'nombre':nombre,
#             'edad':edad,
#             'ocupacion': ocupacion
#             }:
#             print("es un cliente")
#             print(nombre, edad, ocupacion)

#         case {'hamburguesa': titulo,
#             'ingredientes': {'pan' : pan,
#                             'carne' : carne,
#                             'salsa': salsa,
#                             }
#             }:
#             print(f'es una comida con {pan}, {carne} y {salsa}')
#         case _:
#             print('No se es esto :/')



from random import randint

nombre_usuario = input("Dime tu nombre: ")

numero_ramdom = randint(1,101)
contador = 8
while contador != 0:
    print(f'{nombre_usuario} te quedan {contador} vidas\n')
    numero_usuario = int(input("Dime un numero entero: "))
    #otra forma para buscar la condicion
    #if numero_usuario not in range(1,101):
    #    print("El numero no esta en el rango")
    if 0<numero_usuario and numero_usuario<101:
        if numero_usuario<numero_ramdom:
            print(f'{nombre_usuario} intenta con un numero mayor')

        elif numero_usuario>numero_ramdom:
            print(f'{nombre_usuario} intenta con un numero menor')

        else:
            print(f'¡¡¡Felicidades {nombre_usuario} has encontrado el numero!!!\nEl numero encontrado es: {numero_ramdom}')
            break

    else:
        print(f'{nombre_usuario} el numero elegido no esta permitido intenta un numero entre el \"1\" y el \"100\"')
    contador -= 1
    if contador == 0:
        print(f'lo siento perdites el numero era {numero_ramdom}')