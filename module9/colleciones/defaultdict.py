from collections import defaultdict


my_dict = defaultdict(lambda: 'nada') # cuando no se encuentra una clave por defecto asina el valor de nada

my_dict['color'] = "naranja"
print(my_dict['precio'])

print(my_dict)


mi_diccionario = defaultdict(lambda: 'Valor no hallado')
mi_diccionario['edad'] = 44