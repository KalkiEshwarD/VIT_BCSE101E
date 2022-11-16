product_code = int(input())
order_amount = int(input())

if product_code == 1 and order_amount > 1000:
    print(order_amount * 0.90)
elif product_code == 1 and order_amount <= 1000:
    print(order_amount)

if product_code == 2 and order_amount > 750:
    print(order_amount * 0.95)
elif product_code == 2 and order_amount <= 750:
    print(order_amount)
    
if product_code == 3 and order_amount > 500:
    print(order_amount * 0.90)
elif product_code == 3 and order_amount <= 500:
    print(order_amount)
