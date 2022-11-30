# Find the sum of all prime numbers within a given range.

def Prime_Checker(number):
    """
    INPUT:      Integer
    OUTPUT:     Boolean value
    
    DESCRIPTION:    This function takes in an integer as an input and outputs a boolen value to indicate if the entered value is a prime number or not
    """
    Prime = True
    
    for num in range(1, number):
        if num != 1 and num != number and Prime == True:
            if number % num == 0:
                Prime = False

    return Prime

if __name__ == "__main__":
    n_lower = int(input())
    n_higher = int(input())
    
    prime_sum = 0
    
    for num in range(n_lower, n_higher + 1):
        if Prime_Checker(num):
            prime_sum += num

    print(prime_sum)
