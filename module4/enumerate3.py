##Prints on the screen only the indices of those
# names in the list below, beginning with M:

##name_list = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

name_list = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for index, name in enumerate(name_list):
    if name[0]=='M':
        print(index)