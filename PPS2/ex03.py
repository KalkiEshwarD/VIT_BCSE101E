# Write a Python code for the following:
# A list has the objects of maximum 2 strings, 2 complex numbers and 2 integers.
# If at least one integer object is prime, all strings should be reversed and the real part as well as the imaginary part of all the complex numbers should be interchanged
# If at least one string object is a palindrome, all the complex numbers should be conjugated and the integer objects should be negated. 
# If both of the above conditions are satisfied, print the middle element of the list.
# If none of the above conditions satisfied, convert all the strings into list object.

def list_object_type_index_finder(list0):
    """
    DESCRIPTION: It takes in the input as a and gives the output as the position of the strings, complex_numbers and integer objects respectively in a list.
    DEPENDENCIES: Nil

    param: --[list]-- list0 Takes in the input list
    result: --[list]-- obj_index_list This is a 2D list with string, complex_numbers and integers in the format [[string_positions], [complex_nos_positions], [integer_positions]]    
    """
    string_index = []
    complex_index = []
    integer_index = []

    for index in range(len(list0)):
        if type(list0[index]) == str:
            string_index.append(index)
        if type(list0[index]) == int:
            integer_index.append(index)
        if isinstance(list0[index], complex):
            complex_index.append(index)

    obj_index_list = [string_index, complex_index, integer_index]
    return obj_index_list


def list_preparer(list0, string_positions0, integer_positions0):
    """
    DESCRIPTION: It takes in 3 inputs and the returns a list saying if there is a prime number and a palindrome in the list or not.
    DEPENDENCIES: Nil

    param: --[list]-- list0 Takes in the input list
    param: --[list]-- string_positions0 Takes in the positions of the strings within the list
    param: --[list]-- integer_positions0 Takes in the positions of the integers within the list
    result: --[list]-- [{True / False}, {True / False}]
    """
    def palindrome_checker(string0):
        """
        DESCRIPTION: It takes in the input as a string and then gives an output whether the string is a palindrome or not.
        DEPENDENCIES: Nil

        param: --[string]-- string0 Takes in the input string
        result: --[string]-- {Palindrome / Not Palindrome}
        """
        Palindrome = True

        for i in range(0, int(len(string0) / 2)):
            if string0[i].lower() == string0[-1 - i].lower():
                pass
            else:
                Palindrome = False

        return Palindrome

    def Prime_Checker(number0):
        """
        DESCRIPTION: It takes in the input as an integer and outputs whether if it's a prime number or not
        DEPENDENCIES: Nil

        param: --[integer]-- string0 Takes in the input integer
        result: --[Boolean]-- {True / False}
        """
        if number0 < 0:
            number = -number0
        else:
            number = number0

        if number == 0 | number == 1:
            return False

        for num in range(2, number):
            if number % num == 0:
                return False

        return True

    prime_exists = False
    palindrome_exists = False

    for element_index in range(len(integer_positions0) - 1, -1, -1):
        element = list0[integer_positions0[element_index]]
        try:
            if Prime_Checker(element):
                prime_exists = True
                break
        except:
            pass

    for element_index in range(len(string_positions0) - 1, -1, -1):
        element = list0[string_positions0[element_index]]
        try:
            if palindrome_checker(element):
                palindrome_exists = True
                break
        except:
            pass

    return [prime_exists, palindrome_exists]


def strings_list_object_converter(list0, string_positions0):
    """
    DESCRIPTION: It takes in the inputs as a list and string positions and then splits all the strings within the list.
    DEPENDENCIES: Nil

    param: --[list]-- list0 Takes in the input list
    param: --[list]-- string_positions0 Takes in the position of the strings in the list.
    result: --[list]-- list0 Gives the output list
    """
    for index in range(len(string_positions0) - 1, -1, -1):
        curr_string = list0[string_positions0[index]]
        list0.pop(string_positions0[index])
        for element_index in range(len(curr_string)):
            type(string_positions0[index])
            list0.insert(string_positions0[index] + element_index, curr_string[element_index])

    return list0


def conjugator_and_negator(list0, complex_position, integer_position):
    """
    DESCRIPTION: It takes in the input as a list, position of complex numbers, position of integer numbers and conjugates the complex numbers and inverts the sign of the integers in the list.
    DEPENDENCIES: Nil

    param: --[list]-- list0 Takes in the input list
    param: --[list]-- complex_position Takes in the position of the complex numbers within the list.
    param: --[list]-- integer_position Takes in the position of the integers within the list.
    result: --[list]-- list0 Outputs the list after the operation is performed.
    """
    
    try:
        for index in range(len(complex_position) - 1, -1, -1):
            list0[complex_position[index]] = list0[complex_position[index]].conjugate()
    except:
        pass
    try:
        for index in range(len(integer_position) - 1, -1, -1):
            list0[integer_position[index]] = -1 * list0[integer_position[index]]
    except:
        pass

    return list0


def string_and_complex_reverser(list0, string_position0, complex_position0):
    """
    DESCRIPTION: It takes in the input as a list, string_position, complex position and then reverses the elements of the string and then inverts the value of the real and imaginary part of the complex number.
    DEPENDENCIES: Nil

    param: --[list]-- list0 Takes in the input listparam: 
    param: --[list]-- string_position0 Takes in the position of the strings within the list.
    param: --[list]-- complex_position0 Takes in the position of the complex numbers within the list.
    result: --[string]-- {Palindrome / Not Palindrome}
    """
    for index in range(len(string_position0) - 1, -1, -1):
        curr_string = list0[string_position0[index]]
        altering_string = ''
        for char_index in range(len(curr_string) - 1, -1, -1):
            altering_string += curr_string[char_index]
        list0[string_position0[index]] = altering_string

    for index in range(len(complex_position0) - 1, -1, -1):
        curr_complex = list0[complex_position0[index]]
        X = curr_complex.real
        Y = curr_complex.imag
        list0[complex_position0[index]] = complex(Y, X)

    return list0


def main():
    input_stuff = eval(input())

    obj_nos_list = [len(x) for x in list_object_type_index_finder(input_stuff)]
    for length in obj_nos_list:
        if length > 2:
            return 'Invalid Data'

    type_positions = list_object_type_index_finder(input_stuff)
    cases_list = list_preparer(input_stuff, type_positions[0], type_positions[2])

    if cases_list[0] and cases_list[1]:
        return input_stuff[int(len(input_stuff) / 2)]
    elif cases_list[1]:
        input_stuff = conjugator_and_negator(input_stuff, list_object_type_index_finder(input_stuff)[1],
                                             list_object_type_index_finder(input_stuff)[2])
        return input_stuff
    elif cases_list[0]:
        input_stuff = string_and_complex_reverser(input_stuff, list_object_type_index_finder(input_stuff)[0],
                                                  list_object_type_index_finder(input_stuff)[1])
        return input_stuff
    elif not cases_list[0] and not cases_list[1]:
        input_stuff = strings_list_object_converter(input_stuff, list_object_type_index_finder(input_stuff)[0])
        return input_stuff


if __name__ == "__main__":
    result = main()
    print(result)
