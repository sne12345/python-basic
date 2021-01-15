
# list comprehension
list1 = [ i for i in range(1,101) if i % 8 == 0]
print("list1 : ", list1)

# dictionary comprehension
product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = { x : y for x, y in zip(product_list, price_list) }

print(product_dict)