# Given a group of integers. Find the maximum sum of the subsequence of length 3.

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

def max_3(input_list):
    """
    INPUT:      List with elements as integers
    OUTPUT:     Integer
    
    DESCRIPTION:    This function takes in a list of integers as an input and then returns the sum of the first three high valued integers in the list
    """
    compute_list = input_list.copy()
    max_sum = 0
    
    i = 0
    while i < 3:
        max_val = max_finder(compute_list)
        max_sum += max_val
        for index in range(len(compute_list) - 1, -1, -1):
            if compute_list[index] == max_val:
                compute_list = compute_list[:index] + compute_list[index + 1:]
                i += 1
    
    return max_sum

if __name__ == "__main__":
    n = int(input())
    
    integers_list = []
    
    for i in range(n):
        num = int(input())
        integers_list.append(num)
    
    result = max_3(integers_list)
    print(result)
