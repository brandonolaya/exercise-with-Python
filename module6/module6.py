##### open, read, write, close text archive,
# (bookstores or libraries) Path,os


# my_archive = open('Prueba.txt')
# ##el sistema guarda como si la primera linea la sacara y la segunda se combierte en tercera
# my_first_line = my_archive.readline()

# if __name__ == '__main__':
#     print(my_archive.read())
#     ## para quitar un espasio \n
#     print(my_first_line.rstrip())
#     print(my_archive.read())
#     print(my_first_line.upper())
#     ## es bueno cerrar el archivo al final
#     my_archive.close()



# my_archive = open('Prueba.txt')
# def say(archive):
#     for i in archive:
#         print(f"here say: {i}")


# if __name__ == '__main__':
#     say(my_archive)
#     my_archive.close()



# my_archive = open('Prueba.txt')
# def say(archive):
#     ##usar para archivos pequeños
#     lista = archive.readlines()
#     return lista

# if __name__ == '__main__':
#     print(say(my_archive))
#     my_archive.close()

### no se ha modificado el archivo original

## una lectura linea a linea atraves de un for
# file = open('Prueba.txt')
# for line in file:
#     print(line)
# file.close()

#### esta forma es mas cotidiana y no requiere del close()
## automaticamente lo cierra


###para escribir con r+ hace que se agrega nuevo texto pero sin reemplazar el antiguo
# with open('../other/Pruebas.txt', 'r+') as filex:
#     for line in filex:
#         print(line)
# #     ## cuando se escribe agregar saltos de linea al final o al inicio dependiendo
# #     filex.write('\nesto es una mierda')


### con w+ se reescribe el aricho
# with open('Prueba.txt', 'w+') as filex:
#     for line in filex:
#         print(f'esto es lo que tengo en la linea: {line}')

###Si el archivo no se encunetra se cra uno nuevo
# with open('Prueba1.txt', 'w') as archivo:
#     archivo.write('Que hacen las putas nose\n')



# with open('Prueba1.txt', 'w') as archivo:
#     #este metodo escribe el string sin espacios, no es practico
#     lista = ['hola','hijos','de','...']
#     archivo.writelines(lista)
#     for palabra in lista:
#         archivo.writelines(palabra + '\n')


##con la 'a' se para en lo ultimo del archivo, es bueno para registros
# with open('Prueba1.txt', 'a') as archivo:
#     #este metodo escribe el string sin espacios, no es practico
#     lista = ['La','casa','de','los','perros']
#     archivo.writelines(lista)
# #     for palabra in lista:
#         archivo.write(palabra + '\n')

# with open('mi_archivo.txt', 'r+') as archivo:
#     ##escribe pero nio puede leer la ultima linea
#     archivo.write("Hola mis feos\n")
#     for linea in archivo:
#         print(linea)

# archivo = open('mi_archivo.txt')
# print(archivo.read())
# archivo.close()



# archivo  = open("mi_archivo.txt", 'a')
# archivo.write("Nuevo inicio de sesion\n")
# archivo.close()

# archivo  = open("mi_archivo.txt", 'r')
# print(archivo.read())
# archivo.close()



# registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
# archivo = open('registro.txt', 'a')
# for item in registro_ultima_sesion:
#     archivo.writelines(item + '\t')
# archivo.close()

# archivo = open('registro.txt', 'r')
# print(archivo.read())
# archivo.close()







##### Directorios
# import os
##obtener el modulo de directorio actual
# ruta = os.getcwd()
# print(ruta)

# ##cambiar de directorio para acceder a otro lado
# ruta = os.chdir('C:\\Users\\bvola\\OneDrive\\Documents\\python\\otros')
# archivo = open('Prueba.txt', 'r')
# print(archivo.read())
# archivo.close()

##crear una carpeta alfinal le das el nombre
# ruta = os.makedirs('C:\\Users\\bvola\\OneDrive\\Documents\\python\\otros\\graficas')


##resibir por separado
# ruta = 'C:\\Users\\bvola\\OneDrive\\Documents\\python\\otros'
# ## solo da el nombre de la carpeta
# # elemento = os.path.basename(ruta)
# # ## da la ruta completa
# # elemento2 = os.path.dirname(ruta)
# # print(elemento)
# # print(elemento2)
# #da una tupla la cual contiene la ruta, y el nombre de base
# elemento3 = os.path.split(ruta)
# print(elemento3)

##eliminar carpetas
# os.rmdir('C:\\Users\\bvola\\OneDrive\\Documents\\python\\otros\\graficas')


###
# otro_archivo = open('C:\\Users\\bvola\\OneDrive\\Documents\\python\\otros\\Prueba.txt')
# print(otro_archivo.read())
# otro_archivo.close()
## esta forma solo vale para windows




##esta forma sirve para todo sistema operativo lo entienda
# from pathlib import Path
# carpeta = Path('C:/Users/bvola/OneDrive/Documents/python/otros/')
# sin el C: tambien funciona
# carpeta = Path('/Users/bvola/OneDrive/Documents/python/otros/')
# ##es una concatenacion
# archivo = carpeta / 'Prueba.txt'
# mi_archivo = open(archivo)
# print(mi_archivo.read())
# mi_archivo.close()

## otra forma igual ala anterior aunque es menos legible
# archivo2 = Path('/Users/bvola/OneDrive/Documents/python/otros/') / 'Prueba.txt'
# mi_archivo = open(archivo2)
# print(mi_archivo.read())
# mi_archivo.close()




## el pathlib hace la manipulacion mucho mas facil
# from pathlib import Path
# ## no es necesario el OPEN y el CLOSE es mas eficiente
# carpeta = Path('/Users/bvola/OneDrive/Documents/python/otros/Prueba.txt')
# #print(carpeta.read_text())
# #no tiene la invocacion() y de esta manera extra el nombre del archivo
# print(carpeta.name)
# ## suffic quiere decir que en terminael arhivo o tipo de archivo
# print(carpeta.suffix)
# ## da el nombre del elemento independiente
# print(carpeta.stem)



# from pathlib import Path
# ruta = Path('/Users/bvola/OneDrive/Documents/python/otros/Prueba.txt')
# ### comprobar si existe el archivo
# if not ruta.exists():
#     print("create el archicvo pues ...")
# else:
#     print("El perro si existe")



##uso de purewindowspath
# from pathlib import Path, PureWindowsPath
# ruta = Path('/Users/bvola/OneDrive/Documents/python/otros/Prueba.txt')
# ##PureWindowsPath tranforma a una ruta de windows
# ruta_windows = PureWindowsPath(ruta)
# print(ruta_windows)



# from pathlib import Path
# ## sirve para crear rutas para windows ya que queda con barra invertida
# guia = Path("CocaCola", "pura_azucar.txt")
# print(guia)

# ## genera el home
# base = Path.home()
# print(base)

# ## crear una ruta absoluta la primera linea es el directorio principal
# ruta = Path(base,"gaseosas",Path("marcas"),guia)
# print(ruta)
# ## devuelve el directorio ante del ultimo
# print(guia.parent)


# from pathlib import Path
# ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
# carpeta = ruta.parents[1]
# print(carpeta)



# ir a la ruta home
# from pathlib import Path
# ruta_base = Path.home()
# print(ruta_base)


# #creando una ruta
# from pathlib import Path
# ruta = Path("Curso Python","Path","practicas_path.py")
# print(ruta)


# ##conruta absoluta
# from pathlib import Path
# ruta = Path(Path.home(),"Curso Python","Día 6","practicas_path.py")


### Limpiar la consola
## windows('cls')
## otro sistema operativo ('clear')



##### Borrar en consola
# from os import system
# nombre = input('Dime tu nombre: ')
# edad = input("Dime tu edad")
# ##borra la consola
# system('cls')
# print(f'tu nombre es {nombre} y tienes {edad} edad')




# def abrir_leer(archivo):
#     archivo = open(archivo)
#     return archivo.read()


# def sobrescribir(archivo):
#     archivo = open(archivo, 'w')
#     archivo.write("contenido eliminado")


# def registro_error(archivo):
#     archivo = open(archivo, 'a')
#     archivo.write("se ha registrado un error de ejecución")
#     archivo.close()



####Proyect management recipie
