# To access a certain job position, the candidate must be able
# to program in Python and have knowledge of English.

# Creates a conditional structure to evaluate a candidate
# given these conditions, and displays the corresponding message
# on the screen:

# "You meet the requirements to apply"
# "To apply, you need to know how to program in Python and have knowledge of English"
# "To apply, you need to have knowledge of English"
# "To apply, you need to know how to program in Python

speaks_english = True
knows_python = False

if knows_python and speaks_english:
    print("You meet the requirements to apply")
elif (not knows_python) and (not speaks_english):
    print("To apply, you need to know how to program in Python and have knowledge of English")
elif not speaks_english:
    print("To apply, you need to have knowledge of English")
else:
    print("To apply, you need to know how to program in Python")