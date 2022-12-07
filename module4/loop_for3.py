##Given the following list of numbers, perform the sum
#  of all even and odd* numbers separately in the variables
# sum_even and sum_odd respectively:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
counter = 0
sum_pairs = 0
odd_sum = 0
for number in list_numbers:
    if number%2 == 0:
        sum_pairs +=number
    else:
        odd_sum += number

print(f'evens {sum_pairs}\odds {odd_sum}')