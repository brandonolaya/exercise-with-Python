items =[
    {
        'producto': 'camisa',
        'precio': 80
    },
    {
        'producto': 'pantalon',
        'precio': 100
    },
    {
        'producto': 'falda',
        'precio': 3
    }
]

precios = list(map(lambda item: item['precio'],items))
print(precios)
