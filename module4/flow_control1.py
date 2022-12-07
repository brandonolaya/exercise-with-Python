##Using the variables num1 and num2, which are fed
#  with user input (just like in the code already provided):
##Create a control flow structure that compares the values
# ​​of the variables, and returns a result accordingly:


num1 = input("Enter a number:")
num2 = input("Enter another number:")

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")