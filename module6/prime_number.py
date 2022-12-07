
# def contar_primos(numero):
#     primos = []
#     iteracion = 3
#     if numero < 2:
#         return 0
#     while iteracion <= numero:
#         for n in range(3,iteracion):
#             if iteracion % n ==0 :
#                 iteracion += 1
#                 break
#             else:
#                 primos.append(iteracion)
#                 iteracion += 1
#     print(primos)
#     return len(print)



##Numeor primo
def contar_primos(lista):
    mis_primos =[]

    for iteracion in range(2,lista+1):
        primo = True
        for num in range(2,iteracion):
            if iteracion == num:
                break
            elif iteracion%num == 0:
                    primo = False
            else:
                continue
        if primo == True:
            mis_primos.append(iteracion)
    print(mis_primos)
    return len(mis_primos)

if __name__ == '__main__':
    print(contar_primos(50))
    print(5%5 ==0)