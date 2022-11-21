n = int(input())
input_list = input().split(' ')

result_str = ""

for i in range(n):
    if input_list[i][0] == input_list[i][1]:
        result_str += 'D '
        
    if input_list[i][0] == 'R' and input_list[i][1] == 'P':
        result_str += 'B '
        
    if input_list[i][0] == 'R' and input_list[i][1] == 'S':
        result_str += 'A '
    
    if input_list[i][0] == 'S' and input_list[i][1] == 'P':
        result_str += 'A '
        
    if input_list[i][0] == 'S' and input_list[i][1] == 'R':
        result_str += 'B '
        
    if input_list[i][0] == 'P' and input_list[i][1] == 'R':
        result_str += 'A '
        
    if input_list[i][0] == 'P' and input_list[i][1] == 'S':
        result_str += 'B '
        
print(result_str)
