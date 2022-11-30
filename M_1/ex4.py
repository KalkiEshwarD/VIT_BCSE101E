# Given a jumbled set of numbers, your task is to find the first missing natural number.
# The numbers may also contain negative numbers, which must be ignored.
# Find the first missing number (if any) in the range, or display No missing number.

def min_max_finder(input_list):
    """
    INPUT:      List with elements as integers
    OUTPUT:     min_int, max_int
    
    DESCRIPTION:    This function takes in the input in the form of a list and then gives the output of the minimum and the maximum integer that is found in the list.
    """
    
    min_int = input_list[0]    
    max_int = input_list[0]
        
    for number in input_list:
        if number < min_int:
            min_int = number
        if number > max_int:
            max_int = number
        
    return min_int, max_int

def num_finder(input_list):
    """
    INPUT:      List with elements as integers
    OUTPUT:     Integer
    
    DESCRIPTION:    This is a function that takes in a list as input and outputs the first missing natural number from the list
    """
    min_val, max_val = min_max_finder(input_list)
    curr_val = min_val
    
    for i in range(len(input_list)):
        for number in input_list:
            if number == curr_val:
                curr_val += 1
    
    if curr_val < max_val:
        return curr_val
    else:
        return "No missing number"
                
if __name__ == "__main__":
    n = int(input())
    
    integers_list = []
    
    for i in range(n):
        num = int(input())
        if num > 0:
            integers_list.append(num)
        
    result = num_finder(integers_list)
    print(result)
