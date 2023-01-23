# Write a program to mirror a string. 

# Rule for mirroring:
# a) All white space, punctuation, digits character should be left as it is.
# b) All alphabets should be mapped preserving their case like a <->z, b<->y, etc.

# Sample Input
# paradox
# Sample Output
# paizwlc

def string_mirrorer(string0):
    CAPS_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    LOWS_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    list0 = [char for char in string0]
    
    for char_index in range(len(list0)):
        if list0[char_index] in CAPS_LETTERS:
            index = CAPS_LETTERS.index(list0[char_index])
            list0[char_index] = CAPS_LETTERS[25 - index]
        elif list0[char_index] in LOWS_LETTERS:
            index = LOWS_LETTERS.index(list0[char_index])
            list0[char_index] = LOWS_LETTERS[25 - index]
    
    return ''.join(list0)

def main():
    input_stuff = input()
    result = string_mirrorer(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
    
