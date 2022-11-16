# Write a Python program to find out if the given number is abundant.
# An abundant number or excessive number is a number for which the sum of its all factors is greater than the number itself. 
# Example: Input = 12
# Factors/Divisors of 12 (excluding itself) are: 1,2,3,4,6
# Adding all the factors: 
# 1+2+3+4+6 = 12

input_number = int(input())

def factors(number):
    factors_list = []
    
    for num in range(1, number):
        if number % num == 0:
            factors_list.append(num)
        else:
            pass
        
    return factors_list
    
if input_number < sum(factors(input_number)):
    print("Abundant number")
else:
    print("Not Abundant number")
