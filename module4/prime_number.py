def is_prime(num):
    count=0
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        elif number % i == 0:
            count += 1
    if count ==0:
        return True
    else:
        return False


def run(num):
    if is_prime(num):
        print('Is prime number')
    else:
        print("Isn't prime nomber")


if __name__ == "__main__":
    number = int(input('Write a number: '))
    run(number)