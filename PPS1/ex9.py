# Get a DOB from the user which is an 8 digit number. Check whether it is a Lucky number or not by following the steps below:
# Step-1: Calculate the sum of the digits in the odd-numbered positions (the first, third, fifth and seventh digits) and multiply this sum by 3.
# Step-2: Calculate the sum of the digits in the even-numbered positions (the second, fourth, sixth and eighth digits) and add this to the previous result (got in step 1).
# Given Date of Birth is declared as a lucky number, only if the last digit of the result from step 2 is 0.
# Develop an algorithm and write a python program to read the Date of Birth, if the number of digits is not 8 then print “Cannot be processed” and terminate program. If the number of digits is 8 and if the DOB is a lucky number, output the DOB with the message “Lucky Number.” If the number of digits is 8 and if the DOB is not a lucky number, output the DOB with the message “Not a Lucky Number.”
# For example the DOB is 12032003,
# the result from step 1 is 9,
# the result from step 2 is 17
# The output is 12032003, “Not a Lucky Number”.
# For example the DOB is 13101978,
# the result from step 1 is 30,
# the result from step 2 is 50,
# The output is 13101978, “Lucky Number.”
# For example if the DOB is 1110197,
# The output is “Invalid Input”

DOB = input()
if len(DOB) != 8:
    print("Invalid Input")
else:
    odd_list = [int(DOB[0]), int(DOB[2]), int(DOB[4]), int(DOB[6])]
    odd_list_sum = sum(odd_list)
    
    even_list = [int(DOB[1]), int(DOB[3]), int(DOB[5]), int(DOB[7])]
    even_list_sum = sum(even_list)
    
    number = (odd_list_sum * 3) + even_list_sum
    number_str = str(number)
    
    if number_str[-1] == '0':
        print(DOB + ', ' + "Lucky Number")
    else:
        print(DOB + ', ' + 'Not a Lucky Number')
