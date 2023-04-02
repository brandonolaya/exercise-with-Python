import os
import shutil


# print(os.getcwd())##para saber donde me encuentro entre los directorios

# archivo = open('./module9/curso.txt', 'w')
# archivo.write("es una prueba")
# archivo.close()

#print(os.listdir())#lsita todos los archivos

# print(os.walk('./../../../'))
# shutil.move('./module9/curso.txt','./../../python/exercise/module8/curso.txt') #mueve el archivo a donde se quiera


# os.unlink()     #elimina el arichi en la ruta que se le indique
# os.rmdir()      #elimina carpeta vacia
# shutil.rmtree() # elimina todo no recomendado, los archivos no se recuperan

##importan send2trash para que las cosas eliminada queden en la papelera para tener posibilidades de restaurar


ruta = './../../python/exercise/module6/recipes'
for carpeta, subacarpeta, archivo in os.walk(ruta):
    print(f'Ruta de la carpeta: {carpeta}')

    print(f'subcarpetas: ')
    for sub in subacarpeta:
        print(f'\t{sub}')

    print(f'archivos: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')