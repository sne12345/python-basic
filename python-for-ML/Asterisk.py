def astarick_test(a, *args):
    print(a, args)
    print(type(args))

astarick_test(1,2,3,4,5,6)

def astarick_test(a, *args):
    print(a, args)
    print(type(args))

astarick_test(1,*(2,3,4,5,6))




def astarick_test(a, **karg):
    print(a, karg)
    print(type(karg))

astarick_test(1, b=2, c=3, d=4, e=5)







def astarick_test(a, args):
    print(a, *args)     # unpacking
    print(type(args))

astarick_test(1,(2,3,4,5,6))








def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1, (2, 3, 4, 5, 6))


print('----------------')

a, b, c = ([1,2],[3,4],[5,6])
print(a,b,c)

data = ([1,2],[3,4],[5,6])      #unpacking
print(*data)


print('----------------')


def asterick_test(a,b,c,d):
    print(a,b,c,d)

data = {"b":1,"c":2,"d":3}
asterick_test(10, **data)


print('----------------')

for data in zip(*([1,2],[3,4],[5,6])):
    print(sum(data))