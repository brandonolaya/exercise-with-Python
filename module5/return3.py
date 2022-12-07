# Create a function called reverse_word that takes the characters
# of a given word as an argument, reverses the order of its
# characters, and returns them that way and in uppercase.

word = "Python Course"

def invert_word(word):
    word = word[::-1]
    word = word.upper()
    return word

print(invert_word(word))