# Write a program to determine whether a year is a leap year or not.

# A year is a leap year if the following conditions are satisfied: 
# The year is a multiple of 400.
# The year is multiple of 4 and not multiple of 100.

# Sample Input:
#  2000
# Sample Output:
# Leap Year

# Sample Input:
# 2105
# Sample Output
# Not Leap Year

def leap_eval(integer0):
    if integer0 % 400 == 0:
       return True
    else:
        if integer0 % 4 == 0:
            if integer0 % 100 == 0:
                return False
            else:
                return True
        else:
            return False
        


def main():
    input_stuff = int(input())
    result = leap_eval(input_stuff)
    if result:
        print('Leap Year')
    else:
        print('Not Leap Year')


if __name__ == "__main__":
    main()
    
