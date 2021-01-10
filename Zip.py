alist = ['a1','a2','a3']
blist = ['b1','b2','b3']

for a, b in zip(alist, blist):
    print(a,b)

# zip + enumerate
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i,a,b)

# 리스트 활용
cList = [1,2,3]
dList = [10,20,30]
eList = [100,200,300]

result = [sum(x) for x in zip(cList, dList, eList)]
print(result)

# 튜플 활용
aTuple = (1,2,3)
bTuple = (10,20,30)
cTuple = (100,200,300)

result = [sum(x) for x in zip(aTuple, bTuple, cTuple)]
print(result)
