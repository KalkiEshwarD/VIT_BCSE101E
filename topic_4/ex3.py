# Write a program to convert a date to a day of the week, given that day on  01/01/1201 is Monday.
# Day of the week: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
# Leap year conditions:
# A year is a leap year if the following conditions are satisfied: 
# The year is multiple of 400.
# The year is multiple of 4 and not multiple of 100.

input_date = int(input())
input_month = int(input())
input_year = int(input())

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
MONTHS_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_count = 0

def leap_eval(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    return leap
    
if input_year > 1201:
    for year in range(1201, input_year):
        if leap_eval(year):
            days_count += 366
        else:
            days_count += 365

if input_month > 1:
    for month in range(1, input_month):
        days_count += MONTHS_DAYS[month - 1]    
   
if leap_eval(year) and input_month > 2:
    days_count += 1

if input_date > 1:
    days_count += input_date - 1

print(DAYS[days_count % 7])
