# Write a program to find the sum of following series upto two decimal places

# Sample input
# 2 (x)
# 5 (n)
# Sample output
# 7.27

def expression_eval(x0, n0):
    
    final_sum = 0
    
    def factorial(num0):
        fact = 1
        for i in range(1, num0 + 1):
            fact *= i
        return fact
    
    for i in range(0, n0 + 1):
        final_sum += (x0 ** i) / factorial(i)
        
    return final_sum
    

def main():
    input_x = int(input())
    input_n = int(input())
    result = expression_eval(input_x, input_n)
    print(round(result, 2))


if __name__ == "__main__":
    main()
    
