# Given a number ‘n’, write PAC, Algorithm, Flowchart and Python program to print the digits of ‘n’ that divides ‘n’.
# Print the digits in reverse order of their appearance in the number ‘n’. 
# For example, if n is 122 then print 2, 2, 1.
# Use only conditional and iterative statements to write the code.
# If none of the digits divide the number, then print ‘No factors’.

input_number_str = input()
input_number = int(input_number_str)
factors = []

for i in range(len(input_number_str) - 1, -1, -1):
    if input_number % int(input_number_str[i]) == 0:
        factors.append(int(input_number_str[i]))
        
for i in factors:
    print(i, end=' ')
