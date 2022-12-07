import random

lista_numeros = [4,6,15,2,3,7]
def lanzar_moneda():
    return random.choice(['Cara','Cruz'])

def probar_suerte(moneda, lista):
    match moneda:
        case 'Cara':
            print('"La lista se autodestruirá"')
            lista.clear()
            return lista_numeros
        case 'Cruz':
            print('La lista fue salvada')
            return lista

if __name__ == '__main__':
    print(probar_suerte(lanzar_moneda(), lista_numeros))
