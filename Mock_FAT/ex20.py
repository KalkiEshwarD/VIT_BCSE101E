# Write a program to check whether a positive integer is an Armstrong number or not.

# A positive integer of n digits is called an Armstrong number of order n (order is a number of digits) if. 

# abcd… = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + …. 

# Sample input:
# 153
# Output: 
# Yes
# Explanation
# 1*1*1 + 5*5*5 + 3*3*3 = 153
# 153 is an Armstrong number.

# Input
# 120
# Output 
# No
# Explanation
# 1*1*1 + 2*2*2 + 0*0*0 = 9
# 120 is not a Armstrong number.

# Input :
# 1253
# Output :
#  No
# Explanation
# 1*1*1*1 + 2*2*2*2 + 5*5*5*5 + 3*3*3*3 = 723
# 1253 is not a Armstrong Number

def armstrong_number_checker(integer0):
    string_integer0 = str(integer0)
    len_string_integer0 = len(string_integer0)
    
    integer0_digit_sum = 0
    for digit in string_integer0:
        integer0_digit_sum += (int(digit) ** len_string_integer0)
    
    if integer0_digit_sum == integer0:
        return True
    else:
        return False


def main():
    input_stuff = int(input())
    result = armstrong_number_checker(input_stuff)
    if result:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
    
