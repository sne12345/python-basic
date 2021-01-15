products = {"풀" : 1800, "색종이" : 1000}

for product in products.items():
    print("{}은 {}원이다.".format(product[0], product[1]))

list = ['개', '고양이', '사자']
for product in enumerate(list):
    print("{}번째 값은 {}이다.".format(product[0], product[1]))