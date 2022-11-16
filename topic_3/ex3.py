# Write a program to accept three sides of a triangle as the input and print whether the triangle is valid or not.

Valid = True
triangle_sides_length = []

for i in range(0, 3):
    side_length = int(input())
    triangle_sides_length.append(side_length)
    
for i in range(0, 3):
    for k in range(3):
        if i < 2:
            if triangle_sides_length[i] + triangle_sides_length[i + 1] > triangle_sides_length[k]:
                pass
            else:
                Valid = False
        if i == 2:
            if triangle_sides_length[2] + triangle_sides_length[0] > triangle_sides_length[k]:
                pass
            else:
                Valid = False
        
if Valid == True:
    print("Valid")
if Valid == False:
    print("Invalid")
