# Write a Function (WAF) to find roots of a quadratic equation of the form: $ax^2 + bx +c$. Assume a,b,c to be integers.
# a)print the appropriate statements based on
#          i) roots are real and different roots
#         ii) real and same roots
#         iii)complex roots
#
# b) Write the roots in ascending order and upto two decimal places.
#
# Note: You may use math module for finding square root.

import cmath
import math

def quad_root_finder(a, b, c):
    discriminant = b ** 2 - 4*a*c
    try:
        alpha = (- b - math.sqrt(discriminant)) / (2*a)
        beta = (- b + math.sqrt(discriminant)) / (2*a)
    except:
        alpha = (- b - cmath.sqrt(discriminant)) / (2*a)
        beta = (- b + cmath.sqrt(discriminant)) / (2*a)
    return [alpha, beta]


if __name__ == "__main__":
    input_a = int(input())
    input_b = int(input())
    input_c = int(input())

    result = quad_root_finder(input_a, input_b, input_c)

    if result[0] != result[1] and 'j' not in str(result[0]) and 'j' not in str(result[1]):
        print("real and different roots")
        print(round(result[0], 2))
        print(round(result[1], 2))
    elif result[0] == result[1] and 'j' not in str(result[0]):
        print("real and same roots")
        print(round(result[0], 2))
        print(round(result[1], 2))
    else:
        print("complex roots")
        print(result[1])
        print(result[0])
