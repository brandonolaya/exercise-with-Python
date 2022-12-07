archivo = open('mi_archivo.txt', 'w')
archivo.write("Nuevo texto")
archivo.close()

archivo = open("mi_archivo.txt", "r")
print(archivo.read())