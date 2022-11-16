# Write a program to check whether a number is palindrome or not.

Number_list = input()
Palindrome = True

for i in range(0, int(len(Number_list) / 2)):
    if Number_list[i] == Number_list[-1 - i]:
        pass
    else:
        Palindrome = False
        
if Palindrome == True:
    print("Palindrome")

if Palindrome == False:
    print("Not Palindrome")
