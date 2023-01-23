# WAF to find sum of all digits of a number using recursion.

# Sample input
# 163
# Sample output
# 10

def digit_summer(integer_string0):
    if len(integer_string0) > 0:
        if len(integer_string0) > 1:
            final_sum = int(integer_string0[0]) + digit_summer(integer_string0[1:])
            return final_sum
        else:
            final_sum = int(integer_string0[0])
            return final_sum
    
def main():
    input_stuff = input()
    result = digit_summer(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
    
