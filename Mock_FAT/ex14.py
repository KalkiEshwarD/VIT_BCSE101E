# Write a python program to calculate the compound interest on the principal amount, interest rate, compounding frequency per annum, and time provided by the user. 
# Note:Math module is not allowed for this question.

# CI = A -  P

# C.I.	Compound Interest
# P	Principal Amount
# A	Total Accumulated Amount
# r	Rate of Interest 
# n	Compounding Frequency Per Annum
# t	Time (in Years)

# Amount = principal0 * ((1 + ((rate0 / 100)/ freq0)) ** (freq0 * time0))

# In the above formulae, if rate of interest of 7.5%, then r will be 0.075 

# Sample Input
# 1000 (Principal Amount)
# 7.2 (rate of interest in percentage)
# 2 (Compounding frequency per annum)
# 5 (time in years)
# Sample Output
# 424.29

def interest_money_calc(principal0, rate0, freq0, time0):
    Amount = principal0 * ((1 + ((rate0 / 100)/ freq0)) ** (freq0 * time0)) 
    return Amount - principal0

def main():
    input_principal = float(input())
    input_rate = float(input())
    input_compounding_frequency = float(input())
    input_years = float(input())
    
    result = interest_money_calc(input_principal, input_rate, input_compounding_frequency, input_years)
    print(round(result, 2))
    

if __name__ == "__main__":
    main()
    
