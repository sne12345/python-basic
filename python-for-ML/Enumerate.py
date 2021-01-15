for i,j in enumerate(['tic','tac','toe']):
    print(i,j)

myList = ['a','b','c','d']
print(list(enumerate(myList)))

myTuple = {i:j for i,j in enumerate('Apple Banana Computer Dictionary Eraser Food'.split())}
print(myTuple)