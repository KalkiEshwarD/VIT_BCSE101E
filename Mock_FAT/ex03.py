# Given a list of size N-1 integers such that it only contains distinct integers in the range of 1 to N. Find the missing element. 

# Restrictions:

# 1) You are not allowed to use find or sort inbuilt function or create your own function for the same. 
# 2) You are not allowed to use any extra collection type storage data (list, tuple, set, dictionary) except for storing inputs and outputs. For using an extra storage, no marks will be deducted. 
# Basically, your time complexity should be O(n) and space complexity O(1)

def finder(input_list0):
    
    def max_min_sumfinder(input_list0):
        
        max_int = input_list0[0]
        min_int = input_list0[0]
        list_sum = 0
        
        for integer in input_list0:
            if integer > max_int:
                max_int = integer
            if integer < min_int:
                min_int = integer
            list_sum += integer
            
        return [max_int, min_int, list_sum]
        
    max_int, min_int, list_sum = max_min_sumfinder(input_list0)
    
    should_sum = 0
    
    for integer in range(min_int, max_int + 1):
        should_sum += integer
    
    return should_sum - list_sum


def main():
    nums_input = int(input())
    input_list = eval(input())
    result = finder(input_list)
    print(result)


if __name__ == "__main__":
    main()
