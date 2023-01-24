# Write program to input a list and print the frequency of unique numbers in sorted order of the frequency and the integer value in reverse order.

# Sample input
# 7, 7, -2, -7, 9

# Sample output
# (7, 2), (9, 1), (-2, 1), (-7, 1)

def freq_counter(list0):
    freq_dict = {}
    for integer in list0:
        if integer in freq_dict.keys():
            freq = freq_dict[integer]
            freq_dict[integer] = freq + 1
        else:
            freq_dict[integer] = 1

    return freq_dict


def freq_sorter(freq_dict0):
    freq_list = []
    for key, value in freq_dict0.items():
        # print(key, value)
        freq_list.append([key, value])
    # print(freq_list)
    freq_list.sort(key=lambda x: (x[1], x[0]), reverse=True)
    # freq_list.sort(key=lambda x: x[0], reverse=True)
    # print(freq_list)
    return freq_list



def main():
    # input_stuff = list(eval(input()))
    input_stuff = list(eval('7, 7, -2, -7, 9'))
    result = freq_sorter(freq_counter(input_stuff))
    print(result)


if __name__ == "__main__":
    main()
