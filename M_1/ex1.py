# Find a minimum and maximum from a group of integers.

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

if __name__ == "__main__":
    n = int(input())
    
    integers_list = []
    
    for i in range(n):
        num = int(input())
        integers_list.append(num)
    
    min_int, max_int = min_max_finder(integers_list)
    
    print(min_int)
    print(max_int)
