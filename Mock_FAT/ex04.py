# Write a python program to find the IPv4 address from an input string. 

# If the input string contains an valid  IPv4 Address, print the IP address. Otherwise, print 'Invalid IPv4 Address'

# Example of IPV4 address: 
# V.X.Y.Z , Each of V, X,Y,Z can vary from 0 to 255.
# e.g. 192.0.2.126

def IPv4_checker(string0):
    match = re.search(r'((25[0-5]|2[0-4]\d|1\d\d)|\d{1,2})\.((2[0-5][0-5]|2[0-4]\d|1\d\d)|\d{1,2})\.((2[0-5][0-5]|2[0-4]\d|1\d\d)|\d{1,2})\.((2[0-5][0-5]|2[0-4]\d|1\d\d)|\d{1,2})', string0)
    if match:
        return match.group()
    else:
        return 'Invalid IPv4 Address'

def main():
    input_stuff = input()
    result = IPv4_checker(input_stuff)
    print(result)
    

if __name__ == "__main__":
    import re
    main()
    
