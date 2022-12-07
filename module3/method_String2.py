##Join the following list into a string, separating each
# element with a space. It uses the appropriate method of
# lists/strings, and displays the result on the screen.

list_words = "let it be understood account"
list_words = list(list_words.split())
print(list_words)
print(" ".join(list_words))
