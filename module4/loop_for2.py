##Given the following list of numbers, perform the sum
# of all numbers using For loops and store the result of
# the sum in a variable called sum_numbers


list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_numbers = 0
for number in list_numbers:
    sum_numbers += number
print(sum_numbers)