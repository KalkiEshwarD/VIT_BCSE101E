# Write a program to check a prime number.

def Prime_Checker(number):
    Prime = True

    for num in range(1, number):
        if num != 1 and num != number and Prime == True:
            if number % num == 0:
                Prime = False
            else:
                pass
        else:
            pass

    if Prime == True:
        print("IS PRIME")
    else:
        print("NOT PRIME")

Prime_Checker(int(input()))
