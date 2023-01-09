# Write a program to check whether a number is palindrome or not.

def palindrome_checker(string0):
    Palindrome = True

    for i in range(0, int(len(string0) / 2)):
        if string0[i] == string0[-1 - i]:
            pass
        else:
            Palindrome = False

    if Palindrome == True:
        return 'Palindrome'

    if Palindrome == False:
        return "Not Palindrome"



def main():
    number_string = input()        
    result = palindrome_checker(number_sting)
    print(result)
    
if __name__ == "__main__":
    main()
