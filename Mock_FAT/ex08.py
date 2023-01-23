# Write a program to input an integer, and display the day of a week according to following rules.

# 1 → Monday
# 2 → Tuesday
# 3 → Wednesday
# 4 → Thursday
# 5 → Friday
# 6 → Saturday
# 7 → Sunday

# any other integers → Invalid input

# Sample input
# 1
# Sample output
# Monday

# Sample input:
# 8
# Sample output:
# Invalid input

def day_checker(integer0):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if integer0 not in range(1, 8):
        return 'Invalid input'
    else:
        return days[integer0 - 1]
    
def main():
    input_stuff = int(input())
    result = day_checker(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
    
