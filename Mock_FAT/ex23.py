# Write a python program to extract binary numbers from an input string.
# If no valid binary number is present, print "Invalid Data".

def binary_number_finder(string0):
    match = re.search(r'[0-1]+', string0)
    if match:
        return match.group()
    else:
        return 'Invalid Data'
        
        
def main():
    input_stuff = input()
    result = binary_number_finder(input_stuff)
    print(result)
    
    
if __name__ == "__main__":
    import re
    main()
