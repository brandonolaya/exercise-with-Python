suma =lambda num: num*3
suma_superior = lambda num, func: num + func(num)
print(suma_superior(4,suma))