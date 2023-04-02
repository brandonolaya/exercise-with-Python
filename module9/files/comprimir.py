import zipfile


#Comprimiendo el archivo

# my_zip = zipfile.ZipFile('module9/files/file_comprimido.zip', 'w') #ruta + nombre del zip
# my_zip.write('module9/files/textA.txt') #error si no se pone la ruta dentro del comprimido quedara con esas carpetas
# my_zip.write('module9/files/textB.txt')
# my_zip.close()


#descomprimiendo
zip_open = zipfile.ZipFile('module9/files/file_comprimido.zip','r')
zip_open.extractall() #ruta donde lo voy a dejar