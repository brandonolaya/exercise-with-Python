"""
Modulo de patrones inicia con r'XXXXX'
\d cualquier numero
\w culaqui alfanumeroco
\s espacio en blanco
\D no numeros
\W no alfanumero
\S no espacios

+ una o mas veces
{n} se repite n veces
{n,m} se repide entre 3-6 por ejemplo o lo que se le indique
{n, } desde ese numero como minimo hasta donde sea
* 0 o mas
? que aparesca una ves o ninguna
^ excuye un valor al iniciao ejemplo de usar ^\D
$ excliye el valor del final ejemplo de usar \D$
re.findall[`\s]+ construye una lista de palabras
"""
import re





# texto = "Si necesitas ayuda comunicate con el numero 311-884-3300 servicio las 24 horas del dia para ayuda online"
# ##Forma normal de hace una busqueda
# # buscar = "ayuda" in texto
# # print(buscar)

# patron = "ayuda"
# #estas busquedas solo sirver para la primera
# busqueda = re.search(patron, texto) #tra informacion como span, match
# print(busqueda)
# print(busqueda.span())# trae la informacion de que enel indice comienza y finaliza
# print(busqueda.start()) #indice de inicio
# print(busqueda.end()) # indice de final

# busqueda = re.findall(patron, texto)
# print(busqueda) # muestra la lista de las palabra encontradas
# print(len(busqueda)) #como es una lista puedo obtener el largo

# ##para saber en donde se encuentran las busquedas
# for encontrar in re.finditer(patron, texto):
#     print(encontrar.span())

# patron2 = r'\d{3}-\d{3}-\d{4}'
# resultado = re.search(patron2, texto)
# print(resultado.group()) #obtenemos el resultado del match con el patron deseado

# patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')#lo tranforma en una tupla
# resultado2= re.search(patron3, texto)
# print(resultado2.groups())


##control de claves
# clave = input("Clave: ")
# patron = r'\D{1}\w{7}'
# check = re.search(patron, clave)
# print(check)


## busqueda
texto = "Me gusta comer todos los dias de la semana"
buscar = re.search(r'...om..', texto)## la cantidad de puntos es cualqueir cosa con la coincidencia
print(buscar)