def suma_cuadrados(*numeros):
    total = 0
    for num in numeros:
        total += (num**2)
    return total