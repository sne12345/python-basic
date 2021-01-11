ex = [1,2,3,4,5]

# python 3에서는 list를 꼭 붙여주어야 함
f = lambda x: x**2
print(list(map(f,ex)))

f = lambda x, y: x+y
print(list(map(f,ex,ex)))


# lambda에 필터 껴주기
a = list(map(lambda x: x ** 2 if x % 2 == 0 else x, ex))
print(a)

# python 3에서는 list comprehension으로 편하게 쓸 수 있기 때문에 lambda의 사용이 권장되지 않는다.
b = [x ** 2 for x in ex]
print(b)



# Reduce
from functools import reduce
print(reduce(lambda x,y: x+y, [1,2,3,4,5]))


def factorial(n):
    print(reduce(lambda x,y: x*y, range(1,n+1)))

factorial(4)
