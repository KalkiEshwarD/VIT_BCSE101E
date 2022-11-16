# Write a python program to calculate the compound interest on the principal amount using the formulae below:

Principal = int(input())
Rate = float(input())
Time = int(input())

Amount = Principal * (1 + (Rate / 100)) ** Time
Compound_Interest = Amount - Principal

print(Compound_Interest)
