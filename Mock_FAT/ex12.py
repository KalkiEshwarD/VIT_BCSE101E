# WAP to find length of i/p string without using inbuilt function.

# Sample input
# Combination and Permutation
# Sample Output
# 27

def len_string(string0):
    length = 0
    for chat in string0:
        length += 1
    return length


def main():
    input_stuff = input()
    result = len_string(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
    
