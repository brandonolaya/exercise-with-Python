## cuenta bancario que permite depositar retirar usando POO
from os import system

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name



class Customer(Person):
    
    def __init__(self, name, last_name, account_number, deposit=0):
        super().__init__(name, last_name)
        self.account_number = account_number
        self.deposit = deposit


    def __str__(self):
        """da la informacion del cliente
        """
        return f'El nombre del cliente es: {self.name} {self.last_name}\nTiene asociado el numero de cuenta: {self.account_number}\ncon un deposito de {self.deposit}'


    def deposito(self, add_deposit):
        """ En esta funcion se agrega nuevo salda a la cuenta
        """
        self.deposit += add_deposit
        system("cls")
        print(f'Se agregado a la Cuenta')
    

    def retire(self, retire_deposit):
        """esta funcion permite restar la cantidad deseada segun los fondos que se tengan
        en caso de que el retiro sea mayor no lo permitira y si el retiro es menos a cierto cantidad tampoco
        """
        if self.deposit >= retire_deposit and retire_deposit >= 20000:
            self.deposit -= retire_deposit
            print(f"retire hecho te quedan {self.deposit} ")
        elif retire_deposit < 20000:
            print("Minimo retiro 20000")
        else:
            print("Fondos insuficientes")
            


def create_customer():
    """Pide el nombre y el apellido para crear al usuario
    """
    name = input("Cual es tu nombre: ").title()
    last_name = input("Cual es tu apellido: ").title()
    account_number = input("Numero de la cuenta: ")
    system("cls")
    customer = Customer(name, last_name, account_number)
    return customer


def start():
    the_customer = create_customer()
    flag = True

    while flag == True:
        print("""
        [D]. Depositar
        [R]. Retirar
        [V]. Ver fondos
        [S]. Salir
        """)
        option = input().upper()
        system("cls")
        match option:
            case "D":
                depositm = int(input("Monto a depositar: "))
                the_customer.deposito(depositm)
            case "R":
                retirem = int(input("Monto a retirar: "))
                the_customer.retire(retirem)
            case "V":
                print(the_customer.deposit)
            case "S":
                flag = False
            case _:
                "Sos un bola "
    print("¡¡¡Adios sigue haciendo Transsacciones!!!")


if __name__ == "__main__":
    start()