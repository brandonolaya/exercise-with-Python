registro_ultima_sesion = ["krandon", "20/12/2022", "08:17:32 hs", "Sin errores de carga"]
archivo = open('registro.txt', 'a')
for item in registro_ultima_sesion:
    archivo.writelines(item + '\t')
archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())
