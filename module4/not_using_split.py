diccionario ={
        'hola': 1,
        'hijos': 2,
        'de': 3,
        'odin': 4
    }

def run(elementos, lista):
    m = 0
    salida= []
    for nombre , valor in diccionario.items():
        for i in elementos:
            if i == nombre:
                m+= valor
                salida.append(i)
                salida.append(' ')
        if lista == nombre:
            m += valor
            salida.append(i)
    print(m)
    print(salida)

def palabras(dic):
    elementos = []
    lista = ''
    for i in dic:
        if i != ' ':
            lista += i
        else:
            elementos.append(lista)
            lista = ''
    run(elementos, lista)


if __name__ == "__main__":
    dic = str(input('Write dictionarie: '))
    pal(dic)