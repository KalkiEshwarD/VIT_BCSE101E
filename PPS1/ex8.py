# Earthquake Research Institute of Japan has recorded earthquake occurred in the year 2021 using Richter scale.
# Develop PAC, Algorithm, Flowchart and write a Python program to get the ’n’ (number of times) the earthquake has occurred and print the number of times in which the magnitude was low, medium and high.
# The magnitude value is given in microns.
# If the value is less than 5.4(inclusive) in microns then it is low, 5.4 to 7.0 (inclusive) it is medium and more than 7.0 it is high.
# Also, if the number of times recorded is Zero, display as “No earthquake predicted” and if the number of times recorded is negative, display as “Invalid Input”.

earthquake_count = int(input())
earthquake_measure_list = []

low_quake = 0
med_quake = 0
high_quake = 0

for i in range(earthquake_count):
    measure = float(input())
    earthquake_measure_list.append(measure)
    
if earthquake_count < 0:
    print("Invalid Input")
if earthquake_count == 0:
    print("No earthquake predicted")
if earthquake_count > 0:
    for measure in earthquake_measure_list:
        if measure <= 5.4:
            low_quake += 1
        if measure <= 7.0 and measure > 5.4:
            med_quake += 1
        if measure > 7.0:
            high_quake += 1
    
    print(low_quake)
    print(med_quake)
    print(high_quake)
