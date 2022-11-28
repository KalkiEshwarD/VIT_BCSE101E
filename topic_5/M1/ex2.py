# Calculate the mean and variance from the group of integers.
# The result has to be round off to two decimal places.

def mean_variance_finder(input_list):
    """
    INPUT:      List with elements as integers
    OUTPUT:     mean_val and variance_val of the group of integers
    
    DESCRIPTION:    This function takes in a list of integers as the input and outputs the mean and the variance of the data respectively.
    """
    val_sum = 0
    
    for num in input_list:
        val_sum += num
    
    mean_val = val_sum / len(input_list)
    
    variance_val = 0
    for num in input_list:
        variance_val += ((num - mean_val) ** 2 ) / len(input_list)
    
    return mean_val, variance_val


if __name__ == "__main__":
    n = int(input())
    integers_list = []
    
    for i in range(n):
        num = float(input())
        integers_list.append(num)
    
    mean_val, variance_val = mean_variance_finder(integers_list)
    
    print(round(mean_val, 2))
    print(round(variance_val, 2))
