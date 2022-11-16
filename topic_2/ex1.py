# Write a python program to find nth Fibonacci number.

def fib_list_gen(index):
    fib_list = []

    a = 0
    b = 1

    iteration = 0

    while iteration < index:
        fib_list.append(a)
        iteration += 1

        if iteration < index:
            fib_list.append(b)
            iteration += 1
        else:
            break

        if iteration < index:
            c = a + b
            fib_list.append(c)
            iteration += 1
            a = b + c
            b = a + c
        else:
            break

    return fib_list

def fib_index(index):
    fib_list = fib_list_gen(index)

    print(fib_list[-1])

index = int(input())

if index == 0:
    print(0)
else:
    fib_index(index + 1)
