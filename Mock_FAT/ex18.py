# Write a program to convert Celsius into Fahrenheit using the formulae

# F = 9/5* C +32

# Round off the results to 2 decimal places.

# Sample input
# 45.2
# Sample output
# 113.36

def celsius_to_farenheit(celsius_temp0):
    farenheit_temp = (9 / 5) * (celsius_temp0) + 32
    return farenheit_temp


def main():
    input_celsius_temp = float(input())
    result = celsius_to_farenheit(input_celsius_temp)
    print(result)


if __name__ == "__main__":
    main()
    
