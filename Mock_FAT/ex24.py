# Find the sum of first Fibonacci number.
# F0 = 1, F1=1, F2=2

# Sample input
# 4 (N a whole number)
# Sample output
# 12

def fib_sum_finder(terms0):
        
    def fib_gen_list(terms0):
        fib_list = []
        a = 1
        fib_list.append(a)
        b = 1
        fib_list.append(b)
        while len(fib_list) < terms0:
            c = a + b
            fib_list.append(c)
            a = b + c
            fib_list.append(a)
            b = c + a
            fib_list.append(b)
        
        return fib_list
        
    fib_list = fib_gen_list(terms0 + 1)
    fib_sum = 0
    
    for index in range(0, terms0 + 1):
        fib_sum += fib_list[index]
    
    return fib_sum


def main():
    input_stuff = int(input())
    result = fib_sum_finder(input_stuff)
    print(result)


if __name__ == "__main__":
    main()
    
