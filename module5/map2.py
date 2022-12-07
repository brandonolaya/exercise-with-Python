##si unimos otras listas se queda tiene limite de la lista mas pequeña
numbers1 = [9,8,7,6]
numbers2 = [1,2,3]
result = list(map(lambda x,y : x+y,numbers1,numbers2))
print(result)
