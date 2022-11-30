# Write a program to find the sum of series where x and n value is asked from the user.
# 1+ x + x^2/2!+x^3/3! + … +x^n/n!

x = int(input())
n = int(input())

def factorial(num):
    """
    INPUT:      number [integer]
    OUTPUT:     factorial of the number [integer]
    
    DESCRIPTION: Takes in the input in the form of an integer and then outputs the number using iterative approach
    """
    sum = 1
    for i in range(1, num + 1):
        sum *= i
    return sum

def expression_result_finder(x, n):
    sum = 1
    for i in range(1, n + 1):
        sum += (x ** i) / factorial(i)
    return sum
    
print(round(expression_result_finder(x, n), 2))
