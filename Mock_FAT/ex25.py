# WAP to reverse an input string without using an inbuilt function.

# Sample input
# year
# Sample output
# raey

def string_reverser(string0):
    final_string = ''
    for char_index in range(len(string0) - 1, -1, -1):
        final_string += string0[char_index]
    return final_string


def main():
    input_stuff = input()
    result = string_reverser(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
    
