tuple1 = (1, 2, 3, 4)
tuple2 = 1, 2, 3, 4

mylist = [1,2,3,4]
tuple3 = tuple(mylist)

for i in range( len( tuple1) ):
    print( tuple1[i] )

# packing, unpacking
c = (3, 4)
d, e = c    # c의 값을 언패킹하여 d, e에 값을 넣었다
f = d, e    # 변수 d와 e를 f에 패킹

print("{}, {}".format(f[0], f[1]))

# packing
x = 3
y = 5

position = (x,y)
print("x, y로 이루어진 튜플 position의 값은 {}입니다.".format(position))

# 값을 바꾸기
a = 1
b = 2

a, b = b, a

print("a : {}, b : {}".format(a, b))