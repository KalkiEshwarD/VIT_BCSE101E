# Write a program to check whether an integer is prime or not? If the number is prime, then print YES, otherwise print NO.

def prime_checker(integer0):
    for curr_integer in range(2, int(integer0 ** (1 / 2)) + 1):
        if integer0 % curr_integer == 0:
            return False
    
    return True


def main():
    input_stuff1 = int(input())
    input_stuff2 = int(input())
    result = prime_checker(input_stuff2)
    if result:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
    
