# This program calculates the sum of the digits of two numbers entered by the user.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
def find_sum_of_digits_of_the_number(n):
    number_str=str(n)
    sum_of_digits = 0
    for i in range(len(number_str)):
        sum_of_digits+=int(number_str[i])

    return sum_of_digits
    
sum_of_digits_a = find_sum_of_digits_of_the_number(a)
sum_of_digits_b = find_sum_of_digits_of_the_number(b)

print("Sum of digits of the first number:", sum_of_digits_a)
print("Sum of digits of the second number:", sum_of_digits_b)
       