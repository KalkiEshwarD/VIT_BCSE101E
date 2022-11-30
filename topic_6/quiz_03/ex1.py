# Given an string input of numbers plot their frequencies in the descending order of freq of unique elements and in case of a tie in descending order of the elements.

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


def list_sort(input_list):
    """
    INPUT:      List with elements as integers
    OUTPUT:     List

    DESCRIPTION:    This function takes in a list of integers as an input and then returns the sorted list of all the unique integers in the input in descending order.
    """
    compute_list = input_list.copy()
    sorted_list = []
    
    while len(compute_list) != 0:
        max_val = max_finder(compute_list)
        sorted_list.append(max_val)
        for index in range(len(compute_list) - 1, -1, -1):
            if compute_list[index] == max_val:
                compute_list = compute_list[:index] + compute_list[index + 1:]

    return sorted_list

    
def freq_plotter(input_list):
    freq_dict = {}

    for element in input_list:

        if element in freq_dict.keys():
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1

    final_str = ""

    for element in freq_dict.keys():
        final_str += str((element, freq_dict[element])) + ', '

    return final_str[:-2]


if __name__ == "__main__":
    integers_list = []
    input_str_list = input().split(', ')

    for item in input_str_list:
        integers_list.append(int(item))

    result = freq_plotter(integers_list)
    print(result)
