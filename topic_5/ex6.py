str_number = input()
roman_number = ''

ones_list = [[0, ''], [1, 'I'], [2, 'II'], [3, 'III'], [4, 'IV'], [5, 'V'], [6, 'VI'], [7, 'VII'], [8, 'VIII'], [9, 'IX']]
tens_list = [[0, ''], [1, 'X'], [2, 'XX'], [3, 'XXX'], [4, 'XL'], [5, 'L'], [6, 'LX'], [7, 'LXX'], [8, 'LXXX'], [9, 'XC']]
hundreds_list = [[0, ''], [1, 'C'], [2, 'CC'], [3, 'CCC'], [4, 'CD'], [5, 'D'], [6, 'DC'], [7, 'DCC'], [8, 'DCCC'], [9, 'CM']]
thousands_list = [[0, ''], [1, 'M'], [2, 'MM'], [3, 'MMM']]


try:
    thousands_digit = str_number[-4]
    romans_thousands_digit = thousands_list[int(thousands_digit)][1]
    roman_number += romans_thousands_digit
except:
    pass

try:
    hundreds_digit = str_number[-3]
    romans_hundreds_digit = hundreds_list[int(hundreds_digit)][1]
    roman_number += romans_hundreds_digit
except:
    pass

try:
    tens_digit = str_number[-2]
    romans_tens_digit = tens_list[int(tens_digit)][1]
    roman_number += romans_tens_digit
except:
    pass

try:
    ones_digit = str_number[-1]
    romans_ones_digit = ones_list[int(ones_digit)][1]
    roman_number += romans_ones_digit
except:
    pass

print(roman_number)
