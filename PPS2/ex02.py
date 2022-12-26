def password_checker(string0):

    LOWER_CASE_CHAR = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    UPPER_CASE_CHAR = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    NUMS_CHAR = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    SPECIAL_CHAR = ('$', '#', '@')

    passwords_list = string0.split(',')
    acceptable_passwords_list = []

    for password in passwords_list:
    
        lower_case_char_test = 0
        upper_case_char_test = 0
        nums_char_test = 0
        special_char_test = 0
        
        for char in password:
            if char in LOWER_CASE_CHAR:
                lower_case_char_test += 1
            if char in UPPER_CASE_CHAR:
                upper_case_char_test += 1
            if char in NUMS_CHAR:
                nums_char_test += 1
            if char in SPECIAL_CHAR:
                special_char_test += 1

        if lower_case_char_test > 0 and upper_case_char_test > 0 and nums_char_test > 0 and special_char_test > 0:
            acceptable_passwords_list.append(password)
         
    if len(acceptable_passwords_list) == 0:
        return 'invalid'
    else:
        return acceptable_passwords_list
            

def main():
    # input_stuff = input()
    input1 = 'ABd1234@1,aF1#,2w3E*,2We3345'
    input2 = '123,abc,abc@123'
    result1 = password_checker(input1)
    result2 = password_checker(input2)
    print(result1)
    print(result2)

if __name__ == "__main__":
    main()
