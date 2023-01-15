# Find the first few binary numbers from the string

import re

def main():
    match = re.search(r'(?![2-9])\d{1,2}[01]+', input())
    if match:
        print(match.group())
    else:
        print('Invalid Data')

if _name_ == "_main_":
    main()
    
