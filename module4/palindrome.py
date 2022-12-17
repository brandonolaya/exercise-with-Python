def palindromo(word):
    word = word.replace(' ', '')
    word = word.lower()
    invert_word = word[::-1]
    if word == invert_word:
        return True
    else:
        return False


def run():
    word = input("Write a word: ")
    is_palindromo = palindromo(word)
    if is_palindromo == True:
        print('Is palindromo')
    else:
        print("Isn't palindromo")
#point of into python
if __name__ == '__main__':
    run()