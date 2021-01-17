from functools import reduce

def vector_size_check(*vector_variables):
    return all(len(vector_variables[0]) == x for x in [len(vector) for vector in vector_variables[1:]])

def vector_addition(*vector_variables):
    return [sum(x) for x in zip(*vector_variables)]

def vector_substraction(*vector_variables):
    if vector_size_check(vector_variables) == False:
        raise ArithmeticError
    return [elements[0]*2 - sum(elements) for elements in zip(*vector_variables)]

def scalar_vector_production(alpha, *vector_variables):
    return [alpha * x for x in vector_variables[0]]

def matrix_size_check(*matrix_variables):
    return all([len(matrix[0]) == len(matrix_variables[0][0]) and len(matrix) == len(matrix_variables[0]) for matrix in matrix_variables])

def is_matrix_equal(*matrix_variables):
    return all ([all ([len(set(row)) == 1 for row in zip(*matrix)]) for matrix in zip(*matrix_variables)])

def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    return ([[sum(x) for x in zip(*matrix)] for matrix in zip(*matrix_variables)])

def matrix_substraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError

    return ([[x[0] * 2 - sum(x) for x in zip(*matrix)] for matrix in zip(*matrix_variables)])

def matrix_transpose(matrix_variables):
    return ([[element for element in row] for row in zip(*matrix_variables)])

def scalar_matrix_product(alpha, matrix_variable):
    return [[ alpha * x for x in row ] for row in matrix_variable]

def is_product_availability_matrix(matrix_a, matrix_b):
    return  len(matrix_a[0]) == ([len(x) for x in zip(*matrix_b)][0])

def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError

    return [[sum(a * b for a,b in zip(row_a, column_b)) for column_b in zip(*matrix_b)]   for row_a in matrix_a]







print('vector_size_check([1, 4], [4, 3], [6,7])')
print(vector_size_check([1, 4], [4, 3], [6,7]), '\n')

print('vector_addition([1, 3], [2, 4], [6, 7])')
print(vector_addition([1, 3], [2, 4], [6, 7]), '\n')

print('vector_substraction([1,5],[10,4],[4,7])')
print(vector_substraction([1,5],[10,4],[4,7]), '\n')

print('scalar_vector_production(2, [1,2,3])')
print(scalar_vector_production(2, [1,2,3]), '\n')

print('matrix_size_check([[2, 2], [2, 2], [2, 2]],[[2, 5], [2, 1]])')
print(matrix_size_check([[2, 2], [2, 2], [2, 2]],[[2, 5], [2, 1]]), '\n')

matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
print(is_matrix_equal(matrix_x, matrix_y, matrix_y, matrix_y), '\n')

matrix_x = [[2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
print(matrix_addition(matrix_x, matrix_y, matrix_z))

print(matrix_substraction(matrix_x,matrix_y))

print(matrix_transpose([[2,5],[1,1],[2,2]]), '\n')

# 실행결과
matrix_x = [[2, 2], [2, 2], [2, 2]]
matrix_y = [[2, 5], [2, 1]]
matrix_z = [[2, 4], [5, 3]]
matrix_w = [[2, 5], [1, 1], [2, 2]]

print(scalar_matrix_product(3, matrix_x)) #Expected value: [[6, 6], [6, 6], [6, 6]]
print(scalar_matrix_product(2, matrix_y)) #Expected value: [[4, 10], [4, 2]]
print(scalar_matrix_product(4, matrix_z)) #Expected value: [[8, 16], [20, 12]]
print(scalar_matrix_product(3, matrix_w), '\n') #Expected value: [[6, 15], [3, 3], [6, 6]]


# 실행결과
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(is_product_availability_matrix(matrix_y, matrix_z)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_x)) # Expected value: True
print(is_product_availability_matrix(matrix_z, matrix_w)) # Expected value: False //matrix_w가없습니다
print(is_product_availability_matrix(matrix_x, matrix_x),'\n') # Expected value: True


# 실행결과
matrix_x= [[2, 5], [1, 1]]
matrix_y = [[1, 1, 2], [2, 1, 1]]
matrix_z = [[2, 4], [5, 3], [1, 3]]

print(matrix_product(matrix_y, matrix_z)) # Expected value: [[9, 13], [10, 14]]
print(matrix_product(matrix_z, matrix_x)) # Expected value: [[8, 14], [13, 28], [5, 8]]
print(matrix_product(matrix_x, matrix_x)) # Expected value: [[9, 15], [3, 6]]