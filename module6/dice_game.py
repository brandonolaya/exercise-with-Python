
import random
#dados
def lanzar_dados():
    return random.randint(1,6),random.randint(1,6)

def evaluar_jugada(dado1, dado2):
    sumar_dados = dado1 + dado2
    if sumar_dados <=6:
        return f'La suma de tus dados es {sumar_dados}. Basura'
    elif sumar_dados > 6 and sumar_dados<=10:
        return f'La suma de tus dados es {sumar_dados}. muy buena'
    else:
        return f'La suma de tus dados es {sumar_dados}. Pirobo tan loka'
if __name__ == '__main__':
    dado1,dado2 = lanzar_dados()
    print(evaluar_jugada(dado1,dado2))

