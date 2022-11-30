# Write a function to check whether an integer is even or odd.

def odd_number_checker(number):
    odd = True
    if number % 2 == 0:
        odd = False
    return odd


# Write a function to find index of maximum number from a list of integers

def max_int_and_max_index_finder(input_list):
    """
    INPUT:      List with elements as integers
    OUTPUT:     List with output as [max_int, max_index]

    DESCRIPTION:    This function takes in the input in the form of a list and then gives the output of list that contains maximum integer and index of maximum integer found in the list.
    """

    max_int = input_list[0]
    max_index = 0

    for number_index in input_list:
        if input_list[number_index] > max_int:
            max_int = input_list[number_index]
            max_index = number_index

    return [max_int, max_index]


# Write a function to find factorial of a number using iterative approach.

def factorial(num):
    """
    INPUT:      num -- [integer]
    OUTPUT:     fact -- factorial of the number -- [integer]

    DESCRIPTION: Takes in the input in the form of an integer and then outputs the number using iterative approach
    """

    fact = 1

    for i in range(1, num + 1):
        fact *= i
    return fact


# Write a function to find the greatest common divisor of two integers

def greatest_common_divisor_finder(num1, num2):
    """
    INPUT:      num1, num2 -- [integer], [integer]
    OUTPUT:     gcd -- [integer]

    DESCRIPTION: This function takes in two integers as input and outputs the greatest common divisor of the two integers
    """
    gcd = 1

    if num1 > num2:
        min_num = num2
        max_num = num1
    else:
        min_num = num1
        max_num = num2

    if num1 == num2:
        gcd = num1

    for num in range(min_num, 1, -1):
        if max_num % num == 0 and min_num % num == 0 and num > gcd:
            gcd = num

    return gcd


# Write a function to find LCM of two numbers

def least_common_multiple_finder(num1, num2):
    """
    INPUT:          num1, num2 -- [integer], [integer]
    OUTPUT:         lcm -- [integer]
    DEPENDENCIES:   greatest_common_divisor_finder(num1, num2)

    DESCRIPTION: The function takes in two integers for inputs and then outputs the least common multiple in the form of an integer and is dependent upon the function greatest_common_divisor_finder(num1, num2)
    """
    lcm = (num1 * num2) / (greatest_common_divisor_finder(num1, num2))
    return lcm


# Write a function to print n rows of a pascal triangle

def pascal_triangle(rows):
    """
    INPUT:      rows -- [integer]
    OUTPUT:     2D list printing with each element representing the rows of the pascal triangle as a list. -- [2D-list]
    DEPENDICIES: Nil
    
    DESCRIPTION: This function takes in an integer as input for the number of rows and outputs a 2D list as the pascal triangle.
    """
    triangle = [[1]]
    for row_index in range(1, rows):

        row = []

        for element_index in range(row_index + 1):

            if element_index == 0 or element_index == row_index:
                element = triangle[row_index - 1][element_index - 1]

            else:
                element = triangle[row_index - 1][element_index - 1] + triangle[row_index - 1][element_index]
            row.append(element)

        triangle.append(row)

    return triangle
