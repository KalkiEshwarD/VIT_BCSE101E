# WAP to check whether an input string is palindrome or not without using string functions

def palindrome_checker(string0):
    
    def len_string(string0):
        length = 0
        for i in string0:
            length += 1
        return length
    
    string_length = len_string(string0)
    
    for index in range(0, int(string_length / 2)):
        if string0[index] == string0[string_length - index - 1]:
            pass
        else:
            return False
    
    return True


def main():
    input_stuff = input()
    result = palindrome_checker(input_stuff)
    if result:
        print("Yes")
    elif not result:
        print("No")


if __name__ == "__main__":
    main()
    
