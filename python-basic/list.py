list1 = [1,2,3]
list2 = list1 + [4]

n = 4
if n in list2:
    print('{}가 리스트에 있다'.format(n))

del list2[3]
if n in list2:
    print('{}가 리스트에 있다'.format(n))

list3 = list(range(20))
print(list3[-3:-16:-4])
