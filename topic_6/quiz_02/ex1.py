# Write a program to populate a list of integers. And find the sum and max integers from the list.

def max_finder(input_list):
    """
    INPUT:      List with elements as integers
    OUTPUT:     max_int
    
    DESCRIPTION:    This function takes in the input in the form of a list and then gives the output of the maximum integer that is found in the list.
    """
  
    max_int = input_list[0]
        
    for number in input_list:
        if number > max_int:
            max_int = number
        
    return max_int
    
def sum_finder(input_list):
    """
    INPUT:      List with elements as integers
    OUTPUT:     sum_val of the group of integers
    
    DESCRIPTION:    This function takes in a list of integers as the input and outputs the sum of the data.
    """
    sum_val = 0
    
    for num in input_list:
        sum_val += num
    
    return sum_val
    
if __name__ == "__main__":
    
    integers_list = []

    input_str_list = input().split(", ")
    
    for num in input_str_list:
        integers_list.append(int(num))
    
    result = [sum_finder(integers_list),max_finder(integers_list)]
    
    print(result[0])
    print(result[1])
