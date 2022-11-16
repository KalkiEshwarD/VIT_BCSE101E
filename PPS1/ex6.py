# Write a PAC Chart, algorithm, and flowchart for converting the given two- digit number into its corresponding Roman numeral

str_number = input()
roman_number = ''

tens_list = [[0, ''], [1, 'X'], [2, 'XX'], [3, 'XXX'], [4, 'XL'], [5, 'L'], [6, 'LX'], [7, 'LXX'], [8, 'LXXX'], [9, 'XC']]
ones_list = [[0, ''], [1, 'I'], [2, 'II'], [3, 'III'], [4, 'IV'], [5, 'V'], [6, 'VI'], [7, 'VII'], [8, 'VIII'], [9, 'IX']]

tens_digit = str_number[0]
romans_tens_digit = tens_list[int(tens_digit)][1]
roman_number += romans_tens_digit

ones_digit = str_number[1]
romans_ones_digit = ones_list[int(ones_digit)][1]
roman_number += romans_ones_digit

print(roman_number)
