def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave in kwargs.items():
        cantidad += 1
    return cantidad

print(cantidad_atributos(x=1,y=2,z=5))