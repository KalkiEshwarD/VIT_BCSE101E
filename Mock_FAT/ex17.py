# WAP to check whether two input string are isomorphic or not.

# Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping possible for every character of str1 to every character of str2. And all occurrences of every character in ‘str1’ map to the same character in ‘str2’.

# Sample input:
# aab
# xxy
# Sample output:
# True

# Sample input:
# aab
# xyz
# Sample output

def isomorphic_checker(string1, string2):
    corr_char_dict = {}

    if range(len(string1)) != range(len(string2)):
        return False

    for char_index in range(len(string1)):
        if string1[char_index] in corr_char_dict.keys():
            if string2[char_index] != corr_char_dict[string1[char_index]]:
                return False
        else:
            corr_char_dict[string1[char_index]] = string2[char_index]
            
    return True

def main():
    # input_stuff1 = input()
    # input_stuff2 = input()
    input_stuff1 = 'aab'
    input_stuff2 = 'xxy'
    if isomorphic_checker(input_stuff1, input_stuff2) and isomorphic_checker(input_stuff2, input_stuff1):
        result = True
    else:
        result = False
    print(result)


if __name__ == "__main__":
    main()
