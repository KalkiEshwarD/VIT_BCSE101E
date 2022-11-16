# Write a program to find the sum of digit of an integer number.

Number = input()
Sum = 0

for digit in Number:
    Sum += int(digit)
    
print(Sum)
