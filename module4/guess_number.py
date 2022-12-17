import random


def run():
    random_number = random.randint(1,100)
    choose_number = int(input("write a number from 1 to 100: "))
    while choose_number != random_number:
        if choose_number < random_number:
            print("the number is bigger")
        else:
            print("the number is smaller")
        choose_number = int(input("choose another number: "))
    print("¡¡¡Winner you are GREAT!!!")


if __name__ == "__main__":
    run()