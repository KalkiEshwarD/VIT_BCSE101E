# Write a python program to display all numbers within a range except the prime numbers.

def Prime_Checker(number):
    Prime = True
    
    for num in range(1, int(number ** 0.5)):
        if num != 1 and num != number and Prime == True:
            if number % num == 0:
                Prime = False
            else:
                pass
        else:
            pass
    
    return Prime

for num in range(int(input()), int(input()) + 1):
    if not Prime_Checker(num):
        print(num)
