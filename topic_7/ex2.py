# Write a recursive function to find the maximum value from list of integers.

def rec_max(input_list):
    if len(input_list) == 1:
        return input_list[0]
    else:
        max1 = rec_max(input_list[:int(len(input_list)/2)])
        max2 = rec_max(input_list[int(len(input_list)/2):])
        if max1 > max2:
            return max1
        if max2 == max1:
            return max1
        else:
            return max2

if __name__ == "__main__":
    integers_list = [int(item) for item in input().split(', ')]    
    result = rec_max(integers_list)
    print(result)
