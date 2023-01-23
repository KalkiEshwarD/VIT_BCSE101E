# Find the total number of non-empty substrings of an input  string.

# Input : abc 
# Output : 6 
# Explanation Every substring of the given string : “a”, “b”, “c”, “ab”, “bc”, “abc”

# Input : abcd 
# Output : 10 
# Explanation Every substring of the given string : “a”, “b”, “c”, “d”, “ab”, “bc”, “cd”, “abc”, “bcd” and “abcd”

def subs_finder(string0):
    
    num_subs = 0
    
    for i in range(1, len(string0) + 1):
        
        subs_list = []
        for index in range(len(string0)):
            if index + i <= len(string0):
                try:
                    subs_list.append(string0[index: index + i])       
                except:
                    pass
        num_subs += len(subs_list)
    
    return num_subs

def main():
    input_stuff = input()
    result = subs_finder(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
    
