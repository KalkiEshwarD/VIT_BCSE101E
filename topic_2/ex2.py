# Find the maximum number and minimum number from a list of integers without using any inbuilt function.

inputs = int(input())
numbers_list = []

for i in range(inputs):
    number = int(input())
    numbers_list.append(number)

max_num = numbers_list[0]
max_index = []

min_num = numbers_list[0]
min_index = []

for index in range(len(numbers_list)):

    if numbers_list[index] > max_num:
        max_num = numbers_list[index]

    if numbers_list[index] < min_num:
        min_num = numbers_list[index]

for index in range(len(numbers_list)):

    if numbers_list[index] == max_num:
        max_index.append(index)

    if numbers_list[index] == min_num:
        min_index.append(index)

for i in range(len(min_index)):
    print(min_index[i])
    print(min_num)

for i in range(len(max_index)):
    print(max_index[i])
    print(max_num)
