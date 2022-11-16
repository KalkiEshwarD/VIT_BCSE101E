# Write a PAC chart, flowchart, algorithm and python code.
# Calculate the toll charge, by considering kilometers travelled by vehicle.
# Display the toll charge of the two-wheeler to be paid as per chart below.

#kilometers travelled         Charge
# KmTr <=1000KM                   0
# 1000KM <  KmTr <=  10000         50
# 1000KM <  KmTr <=  20000       150
# 2000KM <  KmTr <=  40000       250
# 4000KM <  KmTr <=  60000       350
# KmTr > 60000                    500

kms_travelled = int(input())

if kms_travelled <= 1000:
    charge = 0
if kms_travelled <= 10000 and kms_travelled > 1000:
    charge = 50
if kms_travelled <= 20000 and kms_travelled > 10000:
    charge = 150
if kms_travelled <= 40000 and kms_travelled > 20000:
    charge = 250
if kms_travelled <= 60000 and kms_travelled > 40000:
    charge = 350
if kms_travelled > 60000:
    charge = 500
    
print(charge)
