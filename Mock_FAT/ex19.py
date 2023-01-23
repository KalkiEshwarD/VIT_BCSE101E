# Write a python program to find the file with extension name ".csv".
# The file name will be taken as input.
# If the file type is csv, it will print the file name, otherwise will print "Invalid Input".
# The allowed characters in file name are alphanumeric, and underscore only.

def csv_file_finder(string0):
    match = re.search(r'\w+\.csv', string0)
    if match:
        return match.group()
    else:
        return 'Invalid Input'
def main():
    input_stuff = input()
    result = csv_file_finder(input_stuff)
    print(result)


if __name__ == "__main__":
    import re
    main()
    
