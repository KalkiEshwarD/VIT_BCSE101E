# Write a Function (WAF) to find roots of a quadratic equation of the form: $ax^2 + bx +c$. Assume a,b,c to be integers.
# a)print the appropriate statements based o
#            i) roots are real and different roots
#           ii) real and same roots
#          iii) Complex Roots
# b)  Write the roots in ascending order and upto two decimal places.

# Note: You may use math module for finding square root.
# Sample input:
# 1
# -5
# 6
# Sample Output
# real and different roots
# -3.0
# -2.0

def quad_root_finder(a0, b0, c0):
    
    discriminant = (b0**2) - 4*a0*c0
    
    if discriminant >= 0:
        alpha = (-b0 - math.sqrt(discriminant)) / (2*a0)
        beta = (-b0 + math.sqrt(discriminant)) / (2*a0)
        
        if round(alpha, 2) == round(beta, 2):
            return ['real and same roots', alpha, beta]
        else:
            return ['real and different roots', alpha, beta]
    elif discriminant < 0:
        return ['complex roots', complex(-b0/(2*a0), +math.sqrt(abs(discriminant))/(2*a0)), complex(-b0/(2*a0), -math.sqrt(abs(discriminant))/(2*a0))]
    


def main():
    input_a = float(input())
    input_b = float(input())
    input_c = float(input())
    
    result = quad_root_finder(input_a, input_b, input_c)
    for item in result:
        try:
            print(round(item, 2))
        except:
            print(item)

if __name__ == "__main__":
    import math
    main()
    
