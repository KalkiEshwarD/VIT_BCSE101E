# Write a program to determine whether a person is a senior citizen or not based on gender and age.

# Gender can be either Male or Female, and age is an integer.

# Conditions

# Male:
# age >=60 : Senior Citizen

# Female
# age >55: Senior Citizen 

def senior_checker(gender0, age0):
    if gender0 == 'Male':
        if age0 >= 60:
            return 'Senior Citizen'
        else:
            return 'Not Senior Citizen'
    elif gender0 == "Female":
        if age0 > 55:
            return 'Senior Citizen'
        else:
            return 'Not Senior Citizen'


def main():
    input_gender = input()
    input_age = int(input())
    result = senior_checker(input_gender, input_age)
    print(result)


if __name__ == "__main__":
    main()
    
