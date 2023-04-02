import re

def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron,cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

verificar_cp("Br3200")
verificar_cp("32BR00")