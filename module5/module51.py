### create funcions as def, return, call funtions, *arg, **kwargs,
#  practices the before modules
## last excersice play the hangman game



# dic = {
#     'C1' : 100,
#     'C2' : 500,
#     'C3' : 1500,
# }

# el_pop = dic.popitem()
# print(el_pop)
# print(dic)


#############################################################
#quita solo caracteres a la izquierda hasta que encuentre algo diferente
# txt = ",,,,,ssaawwS.....banana
# x = txt.lstrip(",.aSsw")
# print(x)


########################################################################
#Agrega un elemente y se le puede indicar en donde lo queremos
# frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
# frutas.insert(3,'naranja')
# print(frutas)


##############################################################
#mira que no tenga algo encomun devuelve un bool
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "facebook"}

# z = x.isdisjoint(y)

# print(z)


##############################################################
#funciones

# def saludar(p):
#     '''declarando una funcion para saludar
#     '''
#     print(f"¡Hola {p} del mundo!")

# if __name__ == '__main__':
#     saludar("caballos")


#################################################################
#no se vera en pantalla ya que hace falta el print en el llamado
# def sumar(nombre):
#     return f'Hala {nombre} de la....'
# sumar("perritos")

# #
# def sumar(nombre):
#     return f'Hala {nombre} de la....'
# print(sumar("gaticos"))


#la idea del return es almacenar ese valor para darle uso despues
# def sumar(numero1, numero2):
#     return numero1 + numero2
# resultado= sumar(4,5)
# print(resultado)


#######################################################
#funciones dinamicas
# def chequea_3_cifras(numero):
#     return numero in range(100,1000)

# lista=[55,12,59,36,47,10]
# def check_3_cifras(lista):
#     for n in lista:
#         if n in range(100,1000):
#             return True
#         else:
#             pass
#     return False


# lista=[55,122,59,366,47,10]
# def check_3_cifras(lista):
#     lista_3_cifras =[]
#     for n in lista:
#         if n in range(100,1000):
#             lista_3_cifras.append(n)
#         else:
#             pass
#     return lista_3_cifras

# if __name__ == '__main__':
#     print(check_3_cifras(lista))


##buscando numeros pares
# lista_numeros= [0,1,2,3,4,5,6,7,8,9]
# def cantidad_pares(pares):
#     contador_pares = 0
#     for numero in pares:
#         if numero%2==0:
#             contador_pares +=numero
#     return contador_pares

# if __name__ == '__main__':
#     print(cantidad_pares(lista_numeros))



# precio_panes =[('hojaldre',500), ('Frances',3050),('Queso',6000), ('Hawaiano',1500)]
# def pan_expensive(lista_panes):
#     precio_panes= 0
#     name_pan = ''

#     for pan, precio in lista_panes:
#         if precio > precio_panes:
#             precio_panes = precio
#             name_pan = pan
#     return name_pan, precio_panes

# nombre_pan, pan_precio = pan_expensive(precio_panes)
# if __name__ == '__main__':
#     print(f'El pan mas caro es {nombre_pan} cuyo precio es  {pan_precio}')



###############################################################
#Iteracion de funciones
#perdir algo al usuario,comprobar que le toca hacer,mezcar,lista iniciar

# from random import shuffle

# #lista iniciar
# palitos = ['-','--','---','----']


# #mezclar paitos
# def mezclar(lista):
#     shuffle(lista)
#     return lista


# #probar suerte
# def lucky():
#     inteto = ''
#     while inteto not in ['1','2','3','4']:
#         inteto = input("Elije un numero del 1 al 4: ")
#     return int(inteto)


# #Comprobar
# def check_try(lista,intento):
#     if lista[intento - 1] == '-':
#         print("perdio por marika")
#     else:
#         print("severo por ti")
#     print(f'TE toco {lista[intento-1]}')


# if __name__ == '__main__':
#     check_try(mezclar(palitos),lucky())
#     palito_mix = mezclar(palitos)
#     check = lucky()
#     check_try(palito_mix,check)




# #eliminar duplicados, eliminar numero mas alto, devolver promedio
# lista_numeros=[1,2,5,6,5,3,4,2,3]
# def reducir_lista(lista):
#     return list(set(lista))

# def numero_mayor(lista):
#     lista.pop()
#     return lista

# def promedio(lista):
#     return sum(lista) / len(lista)

# if __name__ == '__main__':
#     print(promedio(numero_mayor(reducir_lista(lista_numeros))))
#     # lista_no_duplicados = reducir_lista(lista_numeros)
#     # lista_sin_mayor= numero_mayor(lista_no_duplicados)
#     # print(promedio(lista_sin_mayor))


# ### misma forma pero don dos funciones y un sort
# lista_numeros = [1,2,15,7,2,8]

# def reducir_lista(lista):
#     lista = list(set(lista))
#     lista.sort()
#     lista.pop(-1)
#     return lista

# def promedio(lista):
#     valor_medio = sum(lista)/len(lista)
#     return valor_medio

# print(promedio(reducir_lista(lista_numeros)))




############################################
##args argumentos es para definir funciones adaptables y no parametros fijos
##itera por todo sin importar su cantidad (debe comenzar con un *)

# def suma(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# def sumar(*numeros):
## usar esta funcion mostrara algo pero no sirve para almacenar
#     return sum(numeros)

# if __name__ == '__main__':
#     print(suma(4,5,4,6,8))
#     print(sumar(8,4,6,2))


# def suma_cuadrados(*numeros):
#     total = 0
#     for num in numeros:
#         total += (num**2)
#     return total

# if __name__ == '__main__':
#     print(suma_cuadrados(5,5,3))


# def suma_absolutos(*numeros):
#     total = 0
#     for num in numeros:
#         total += abs(num)
#     return total

# if __name__ == '__main__':
#     print(suma_absolutos(-5,5,-15))



# def numeros_persona(nombre,*numeros):
#     total = sum(numeros)
#     return f'{nombre}, la suma de tus numeros es {total}'

# if __name__ == '__main__':
#     print(numeros_persona(input("Cual es tu nombre: "), 5,5))



###############################################
##**kwargs es una palbra clase se usa para diccionarios

# def suma(**kwargs):
#     print(type(kwargs))
# ##Esto no es un diccionario, pero la funcion lo vuevle un diccionario
# if __name__ == '__main__':
#     suma(x=4,y=3,z=2)


# def suma(**kwargs):
#     total = 0
#     for clave, valor in kwargs.items():
#         print(f'{clave} = {valor}')
#         total += valor
#     return total

# if __name__ == '__main__':
#     print(suma(x=4,y=3,z=2))


# def suma_cosas(num1,num2, *args, **kwargs):
#     print(f'el primer valor es {num1}')
#     print(f'el segundo valor es {num2}')

#     for arg in args:
#         print(f'arg = {arg}')

#     for clave,valor in kwargs.items():
#         print(f'{clave} = {valor}')

#     return sum(args)

# if __name__ == '__main__':
#     numeros =[700,400,500,600,200,300]
#     diccionario = {
#         'c':'uno',
#         'x':'dos',
#         'y':'tres'
#     }
#     #se debe especificar la variable si es un args o kwargs con los asteriscos
#     print(suma_cosas(4,5,*numeros,**diccionario))


# def cantidad_atributos(**kwargs):
#     cantidad = 0
#     total = 0
#     for clave, valor in kwargs.items():
#         cantidad += 1
#         total += valor
#     return cantidad, total

# if __name__ == '__main__':
#     print(cantidad_atributos(x=2,t=5,k=7))

# def lista_atributos(**kwargs):
#     lista =[]

#     for valor in kwargs.values():
#         lista.append(valor)
#     #agregara todo a una lista como una tupla
#     # for valor in kwargs.items():
#     #     lista.append(valor)
#     return lista


# if __name__ == '__main__':
#     print(lista_atributos(x=5,y=10,t=2))



# def describir_persona(**kwargs):
#     for clave,valor in kwargs.items():
#         print(f'Características de {clave}:')
#         print(f'{valor}\n')

# if __name__ == '__main__':
#     dic = {
#         'brandon': {
#             'ojos' : 'negro',
#             'pelo' : 'negro'
#         },
#         'fran':{
#             'ojos' : 'verdes',
#             'pelo' : 'azul'
#         },
#         'ichigo':{
#             'ojos' : 'naranja',
#             'pelo' : 'naranja'
#         }
#     }
#     describir_persona(**dic)



# def devolver_distintos(*numeros):
#     contador= list(numeros)
#     suma = sum(numeros)
#     if suma< 10:
#         return min(contador)
#     elif suma > 15:
#         return max(contador)
#     else:
#         contador.sort()
#         return contador[1]


# if __name__ == '__main__':
#     print(devolver_distintos(
#     int(input("escribra el primer numero: ")),
#     int(input("escribra el segundo numero: ")),
#     int(input("escribra el tercer numero: "))))




# def palabra_valor(txt):
#     palabra = txt.lower()
#     palabra = list(set(palabra))
#     palabra.sort()
#     return palabra


# if __name__ == '__main__':
#     print(palabra_valor("Entretenido"))



########
#comparacion de una pocicion con la otra
# def consecutivo(*numeros):
#     who_is = 0

#     for elemento in numeros:
#         ##resuelve el problema cuando no se a encontrado nada y esta en el ultimo
#         if who_is + 1 == len(numeros):
#             return False
#         elif numeros[who_is] == 0 and numeros[who_is + 1 ] ==0:
#             return True
#         else:
#             who_is += 1
#     return False


# if __name__ == '__main__':
#     print(consecutivo(4,0,5,2,0,4,8,0,6))