n =  input()

input_list = []
reverse_list = []
sum = 0 

for char in n:
    input_list.append(char)
    sum += int(char)
    
for i in range(len(input_list) - 1, -1, -1):
    reverse_list.append(input_list[i])
    
final_string = ""

for char in reverse_list:
    final_string += char

print(final_string)
print(sum)
