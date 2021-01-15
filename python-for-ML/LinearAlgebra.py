u = [2,2]
v = [2,3]
z = [3,5]

print("vector의 덧셈")
result = [sum(t) for t in zip(u,v,z)]
print(result)

print("vector의 뺄셈")
result = [x-y-z for x,y,z in zip(u,v,z)]
print(result)




print("scalar-vector product")
u = [1,2,3]
v = [4,4,4]
alpha = 2

result = [alpha * sum(z) for z in zip(u, v)]
print(result)





print("Matrix addition")
matrix_a  = [[3, 6], [4, 5]]
matrix_b  = [[5, 8], [3, 7]]

result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)


print("Scalar-Matrix Product")
matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]

print(result)




print("Matrix Transpose")
matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [[element for element in t] for t in zip(*matrix_a)]

print(result)




print("Matrix Product")
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b))
          for column_b in zip(*matrix_b)] for row_a in matrix_a]
print(result)


print('zero one two three'.split())
listA = [i.upper() for i in ['a','b','c']]
print(listA)