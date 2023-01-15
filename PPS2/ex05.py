# Calculate the following numbers in numerology using below table. (using Set only)
# Pythagorean numerology number
# 1 2 3 4 5 6 7 8 9
# A B C D E F G H I
# J K L M N O P Q R
# S T U V W X Y Z
# a. Destiny number (sum of the numerical value assigned to each letter in the name up to single digit) Ex: TEENA (2+5+5+5+1=18=1+8=9)
# b. Soul urge number/Heart’s desire number (sum of the numerical value assigned to each VOWEL in the name up to single digit)
# Ex: TEENA (5+5+1=11=2)
# c. Dream number (sum of the numerical value assigned to each CONSONANT in the name up to single digit)
# Ex: TEENA (2+5=7)

PNN_C1 = {1, 'A', 'J', 'S'}
PNN_C2 = {2, 'B', 'K', 'T'}
PNN_C3 = {3, 'C', 'L', 'U'}
PNN_C4 = {4, 'D', 'M', 'V'}
PNN_C5 = {5, 'E', 'N', 'W'}
PNN_C6 = {6, 'F', 'O', 'X'}
PNN_C7 = {7, 'G', 'P', 'Y'}
PNN_C8 = {8, 'H', 'Q', 'Z'}
PNN_C9 = {9, 'I', 'R'}

VOWELS = {'A', 'E', 'I', 'O', 'U'}


def num_breakdown_func(number0):
    """
    INPUT:      number0 [integer]
    OUTPUT:     number0 [integer]

    DESCRIPTION:    This is a recursive function that breaks down a number into it's constituents, sums its digits and repeats the process till the end result is a single digit number which it returns.
    DEPENDENCIES:   Nil
    """
    if len(str(number0)) == 1:
        return number0
    else:
        digits_sum = 0
        nums_breakdown_list = [int(element) for element in str(number0)]
        for digit in nums_breakdown_list:
            digits_sum += digit
        return num_breakdown_func(digits_sum)


def destiny_number_finder(string0):
    """
    INPUT:      string0 [string]
    OUTPUT:     final_num [integer]

    DESCRIPTION:    This is a function that breaks down the string into it's constitutes and finds the corresponding numerology number from the table and returns the sum of the numbers.
    DEPENDENCIES:   num_breakdown_func(number0) [function], corr_num_finder(element0) [function]
    """
    final_num = 0
    for char in string0:
        final_num += corr_num_finder(char)
    return num_breakdown_func(final_num)


def soul_urge_number_finder(string0):
    """
    DESCRIPTION: This is a function that takes input in the form of a string and then finds the corresponding number for the vowels
    DEPENDENCIES: num_breakdown_func(number0) [function], corr_num_finder(element0) [function]

    @param: --[string]-- string0 Takes in the input string
    @result: --[integer]-- num_break_down_func(final_num) Outputs the final number after undergoing alterations by num_break_down_func
    """

    final_num = 0
    for char in string0:
        if char in VOWELS:
            final_num += corr_num_finder(char)
    return num_breakdown_func(final_num)



def dream_number_finder(string0):
    """
    DESCRIPTION: Takes in the input in form of a string and then finds the corresponding pythagorean number using the corr_num_finder.
    DEPENDENCIES: num_breakdown_func(number0) [function], corr_num_finder(element0) [function]

    @param: --[string]-- string0 Takes in the input in the form of a string
    @result: --[integer] num_break_down_func(final_num) Outputs the final number after undergoing alterations by num_break_down_func
    """
    final_num = 0
    for char in string0:
        if char not in VOWELS:
            final_num += corr_num_finder(char)
    return num_breakdown_func(final_num)

def corr_num_finder(char0):
    """
    DESCRIPTION: Takes in the input in the form of a string and the ouputs the corresponding pythogorean number using the PNN tables.
    DEPENDENCIES: PNN_TABLE_C1, PNN_TABLE_C2, PNN_TABLE_C3, PNN_TABLE_C4, PNN_TABLE_C5, PNN_TABLE_C6, PNN_TABLE_C7, PNN_TABLE_C8, PNN_TABLE_C9, (CONSTANT)
    
    @param: --[string]-- char0 Takes in the input in the form of a string
    @result: --[integer]-- element Finds the corresponding pythagorean integer and outputs it.
    """
    if char0 in PNN_C1:
        for element in PNN_C1:
            if type(element) == int:
                return element
    if char0 in PNN_C2:
        for element in PNN_C2:
            if type(element) == int:
                return element
    if char0 in PNN_C3:
        for element in PNN_C3:
            if type(element) == int:
                return element
    if char0 in PNN_C4:
        for element in PNN_C4:
            if type(element) == int:
                return element
    if char0 in PNN_C5:
        for element in PNN_C5:
            if type(element) == int:
                return element
    if char0 in PNN_C6:
        for element in PNN_C6:
            if type(element) == int:
                return element
    if char0 in PNN_C7:
        for element in PNN_C7:
            if type(element) == int:
                return element
    if char0 in PNN_C8:
        for element in PNN_C8:
            if type(element) == int:
                return element
    if char0 in PNN_C9:
        for element in PNN_C9:
            if type(element) == int:
                return element


def main():
    input_stuff = input()
    print(destiny_number_finder(input_stuff))
    print(soul_urge_number_finder(input_stuff))
    print(dream_number_finder(input_stuff))


if __name__ == "__main__":
    main()
