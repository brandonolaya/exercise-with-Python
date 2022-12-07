def suma_absolutos(*numeros):
    total = 0
    for num in numeros:
        total += abs(num)
    return total