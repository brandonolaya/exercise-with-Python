##Using the max(), min() and dictionary methods,
# get the minimum value from the following dictionary:

diccionario_edades = {
    "Carlos":55,
    "María":42,
    "Mabel":78,
    "José":44,
    "Lucas":24,
    "Rocío":35,
    "Sebastián":19,
    "Catalina":2,
    "Dario":49
    }
minimum_age = min(diccionario_edades.values())
last_name = max(diccionario_edades)
print(f'la edad minima es {minimum_age} y el ultimo nombre es {last_name}')
