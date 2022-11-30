# Write a program to do take input and populate two lists.
# Each list is a 2-D matrix, so you have to consider as list of list.
# Your program should print the result of elements wise addition of the two list.
# If the to list does not match in dimension, print ADDITION NOT POSSIBLE

if __name__ == "__main__":

    dim1 = []
    dim2 = []

    str_dim1 = input().split('*')
    str_dim2 = input().split('*')

    for dim in str_dim1:
        dim1.append(int(dim))
    for dim in str_dim2:
        dim2.append(int(dim))

    mat1 = []
    mat2 = []

    for row_index in range(dim1[0]):
        row = []
        str_row = input().split(', ')

        for item in str_row:
            row.append(int(item))

        mat1.append(row)

    for row_index in range(dim2[0]):
        row = []
        str_row = input().split(', ')

        for item in str_row:
            row.append(int(item))

        mat2.append(row)

    if dim1 != dim2:
        print("ADDITION NOT POSSIBLE")
    else:
        mat_sum = []

        for row_index in range(dim1[0]):
            row = []

            for element_index in range(dim1[1]):
                row.append(mat1[row_index][element_index] + mat2[row_index][element_index])

            mat_sum.append(row)

        for row in mat_sum:
            s = ""
            for element_index in range(len(row)):
                s += str(row[element_index])
                if element_index == len(row) - 1:
                    pass
                else:
                    s += ', '

            print(s)
