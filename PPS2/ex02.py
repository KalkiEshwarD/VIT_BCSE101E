# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users (using tuples only)
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
# If none of the password is valid, you should print “invalid”.

def password_checker(string0):
    """
    INPUT:      string0 [string]
    OUTPUT:     --Multiple Outputs-- [string]

    DESCRIPTION:    This functions takes in a string with comma separated values as passwords and returns a string with comma separated values as valid passwords.
    DEPENDENCIES:   Nil
    """
    LOWER_CASE_CHAR = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z')
    UPPER_CASE_CHAR = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z')
    NUMS_CHAR = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    SPECIAL_CHAR = ('$', '#', '@')

    passwords_list = string0.split(', ')
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

        if lower_case_char_test > 0 and upper_case_char_test > 0 and nums_char_test > 0 and special_char_test > 0 and ' ' not in password:
            acceptable_passwords_list.append(password)

    if len(acceptable_passwords_list) == 0:
        return 'invalid'
    else:
        return ', '.join(acceptable_passwords_list)


def main():
    input_stuff = input()
    result = password_checker(input_stuff)
    print(result)


if __name__ == "__main__":
    main()

