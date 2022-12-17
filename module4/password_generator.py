import random

def password_generator():
    uppercase = ['A','B','C','D','E','F','G', 'H', 'I', 
                'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 
                'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lowcase = ['a','b','c','d','e','f','g','h', 'i', 'j',
                'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 
                's', 't', 'u', 'v', 'x', 'y', 'z']
    caracters = ['!','"','#','$','%','%','&']
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    change_caraters = uppercase + lowcase + caracters + numbers

    password = []

    for i in range(12):
        ramdon_caracter = random.choice(change_caraters)
        password.append(ramdon_caracter)

    password = ''.join(password)
    return password

def run():
    password = password_generator()
    print('You password is : ' + password)


if __name__ == '__main__':
    run()