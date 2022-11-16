# Draw a flowchart and construct a python program to accept the monthly  income of an employee and display the income tax to be paid at the end of the year according to the following criteria:
#
# Annual income (in Rs)                            Income Tax
# > 1000000                                        4 %
# > 500000 and <= 1000000                          2 %
# <= 500000                                        NIL

annual_income = int(input())

if annual_income > 1000000:
    tax_percentage = 0.04
if annual_income > 500000 and annual_income <= 1000000:
    tax_percentage = 0.02
if annual_income <= 500000:
    tax_percentage = 0.00
    
if tax_percentage == 0:
    print("NIL")
else:
    print(int(annual_income * tax_percentage))
