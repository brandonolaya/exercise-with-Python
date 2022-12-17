menu = """
welcome to convert coins
X country coin to dolar
1. - Colombian pesos
2. - Mexican pesos
3. - Rublos
4. - Euros
Choose an option: """
def conversor(name,dollar):
    money = float(input("How much "+ name + " pesos do you have: "))
    dollar = money/dollar
    dollar = round(dollar, 2)
    dollar = str(dollar)
    print("Do you have $" + dollar + " dollars")

option = input(menu)

if option == '1':
    conversor("Colombian",4025)
elif option == '2':
    conversor("Mexican", 20.28)
elif option == '3':
    conversor("rublos", 68.25)
elif option == '4':
    conversor("Euro",0.95)
else:
    print("enter a menu option. ¡¡¡PLEASE!!!")