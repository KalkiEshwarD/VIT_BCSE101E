# Write program to input a list and print the frequency of unique numbers in sorted order of the frequency and the integer value in reverse order.

# Sample input
# 7, 7, -2, -7, 9

# Sample output
# (7, 2), (9, 1), (-2, 1), (-7, 1)

def freq_plotter(list0):
    freq_dict = {}
    for integer in list0:
        if integer in freq_dict.keys():
            freq = freq_dict[integer]
            freq_dict[integer] = freq + 1 
        else:
            freq_dict[integer] = 1
    
    
    freq_list = list(set{list(freq_dict.values())})
    
    for freq in freq_list:
        keys = [dict_keys for dict_keys, dict_values in freq_dict.items()]
        
    return freq_dict
    

def main():
    input_stuff = list(eval(input()))
    result = freq_plotter(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
    
