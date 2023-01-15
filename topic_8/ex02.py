# Find the file name of the file with extension .csv

import re

def main():
    match = re.search(r'(?! )\w*\.csv', input())
    if match:
        print(match.group())
    else:
        print('Invalid Input')

if _name_ == "_main_":
    main()
