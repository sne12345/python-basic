names = ['철수', '영희', '영수']
del(names[1])
for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))

list = ['개', '고양이', '사자']
for product in enumerate(list):
    print("{}번째 값은 {}이다.".format(product[0], product[1]))