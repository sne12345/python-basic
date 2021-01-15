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
    # print(len([*matrix_variables[0][0]]))
    #
    # li = [len(i) for i in zip(*matrix_variables[0])]
    # print(li[0])
    return all([len(matrix[0]) == len(matrix_variables[0][0]) for matrix in matrix_variables])


print('vector_size_check([1, 4], [4, 3], [6,7])')
print(vector_size_check([1, 4], [4, 3], [6,7]), '\n')

print('vector_addition([1, 3], [2, 4], [6, 7])')
print(vector_addition([1, 3], [2, 4], [6, 7]), '\n')

print('vector_substraction([1,5],[10,4],[4,7])')
print(vector_substraction([1,5],[10,4],[4,7]), '\n')

print('scalar_vector_production(2, [1,2,3])')
print(scalar_vector_production(2, [1,2,3]), '\n')


print(matrix_size_check([[1, 2], [2, 2], [3, 2]],[[2, 5], [2, 1]]))

