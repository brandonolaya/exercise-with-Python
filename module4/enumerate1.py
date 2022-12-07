
# Prints sentences like the following on the screen:

# '{name} is found at index {index}'

# Where name should be each of the names in the list below,
# and the index, obtained by enumerate()


name_list = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for index,name in enumerate(name_list):
    print(f'{name} is found at index {index}')