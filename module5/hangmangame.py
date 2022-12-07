####################################################
###Juego del Ahorcado
import random
lista_palabras =["computador","juego","televisor","procesador","comedor"]
def palabra_alazar(lista):

    palabra = random.choice(lista)
    palabra = palabra.upper()
    normal = palabra
    palabra = list(palabra)
    return lista_guiones(palabra,normal)


def lista_guiones(palabra,normal):
    guiones = []
    for i in palabra:
        guiones.append("_")
    return validar(palabra,guiones,normal)


def validar(palabra,guiones,normal):
    """This function using two list palabra, guiones, for comparte if are twice equals
    normal it is the word not in list
    It's necessary create variable of life for the game and show errors
    """
    vidas = 6
    errores =[]
    print(f'La palabra es de {len(guiones)} letras\n{guiones}\n')


    while vidas !=0:
        print(f'tienes {vidas} vidas\n')
        cont = 0
        if set(palabra) == set(guiones):
            print("FELICIDADES HAS GANADO")
            break

        letra = input("Escribe una letra: ").upper()
        if letra in palabra:
            for elemento in palabra:
                cont +=1
                if elemento == letra:
                    guiones[cont-1] = letra
        else:
            errores.append(letra)
            vidas -= 1
            print(errores)


        print(guiones)

    if vidas ==0:
        print(f"PERDISTE la palabra era: {normal}")


if __name__ == '__main__':
    palabra_alazar(lista_palabras)
