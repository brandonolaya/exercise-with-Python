# Create the zip with the translations of the numbers
# from 1 to 5 in Spanish, Portuguese and English
# (in the same order), and convert the generated object
# into a list stored in the numbers variable:

# one / um / one
# two / two / two
# three / three / three
# four / four / four
# five / five / five

number_spain = ['uno', 'dos','tres','cuatro','cinco']
number_italy = ['um','dois','três','quatro','cinco']
number_english = ['one','two','three','four','five']

numbers = list(zip(number_spain,number_italy,number_english))

print(numbers)