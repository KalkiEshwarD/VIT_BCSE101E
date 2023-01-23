# Write a recursive function to find the maximum value from list of integers.

# Sample input
# 1, 3, 7, 19, 40, 12, 16

# Sample output:
# 40

def rec_max_int(list0):
    if len(list0) > 0:
        max_int = list0[0]
        res = rec_max_int(list0[1:])
        if res is not None:
            if max_int < res:
                max_int = res
        return max_int


def main():
    input_stuff = input().split(', ')
    for element_index in range(len(input_stuff)):
        input_stuff[element_index] = int(input_stuff[element_index])
    result = rec_max_int(input_stuff)
    print(result)
    

if __name__ == "__main__":
    main()
    
