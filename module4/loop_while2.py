# Create a While Loop that subtracts one by one the numbers
# from 50 to 0 (both numbers included) with the following
# additional conditions:

# - If the number is divisible by 5, display that number on the screen
# -If the number is not divisible by 5, continue


num = 50
while num >= 0:
    if num%5 ==0 :
        print(num)
        num -= 1
    else:
        num -= 1