#  Petrol is collected for Indian Oil Corporation for sales from nearest ‘n’ storage points to the Collection point.
# Given the amount of petrol from ‘n’ storage points in liters(L) and milli liters (mL), write a PAC chart, flowchart, algorithm and python code to compute the total quantity of oil in the collection point.
# For example, if oil comes from 3 bunks in quantities 2 L 300 mL, 3 L 700 mL and 4 L 600 mL then the total quantity of oil in collection is 10 L 600 mL.

storage_points = int(input())
quantity_list = []
total_quantity = 0

for i in range(storage_points):
    L_qty = int(input())
    mL_qty = int(input()) * 0.001
    qty = L_qty + mL_qty
    total_quantity += qty
    
L_total_qty = int(total_quantity)
mL_total_qty = int(round((total_quantity - L_total_qty) * 1000, 0))

print(L_total_qty)
print(mL_total_qty)
