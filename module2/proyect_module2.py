#asignar valor a las variables


#format no es legible pero si practico
#color = "rojo"
#matricula = "ASD 567"
#print("mi auto es {} y de matricula {}".format(color,matricula))
#print(f'mi auto es {color} y de matricula {matricula}')


######################################################3
#operaciones
#x = 5
#y = 2
#z = 11
#n = 49
#print(f'{x} mas {y} es igual a {x+y}')
#print(f'{x} menos {y} es igual a {x-y}')
#print(f'{x} pro {y} es igual a {x*y}')
#print(f'{x} dicidido {y} es igual a {x/y}')
#es una divicion exacta
#print(f'{z} dividido al piso de {y} es igual a {z//y}')
#print(f'{z} modulo de {y} es igual a {z%y}')
#print(f'{x} elevado a la {y} es igual a {x**y}')
#print(f'{y} elevado a la {z} es igual a {y**z}')
#print(f'La raiz cuadrada de {n} es {n**0.5}')




################################################
#redondeo
#print(round(10/3,2))

#valor = 10.676767
#print(round(valor))
#print(round(5**0.5,4))


#num1=13.87
#print(round(num1))
#print(int(num1))
#num1 = round(13/2,0)
#print(num1)



#Proyects comisiones para saber cuantas son mis comisiones 13%
nombre = input("cual es tu nombre: ")
ventas = float(input("Cuantas ventas hiciste: "))
print(f'el trabajador {nombre} tiene una comision de {round(ventas*0.13,2)}')
