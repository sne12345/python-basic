# 중복을 허용하지 않는다.
s1 = set([1,2,3,3])
print(s1, '\n')

# 순서가 없다.
s2 = set("Hello")
print(s2, '\n')

# 교집합 구하기
s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
print(s3 & s4, '\n')

# 합집합 구하기
print(s3 | s4, '\n')

# 차집합 구하기
print(s1 - s2, '\n')

# 집합에 값 한 개 추가하기
s1.add(7)
print(s1, '\n')

# 집합에 여러 개 값 추가하기
s1.update([4,5,6])
print(s1, '\n')


# 특정 값 제거하기
s1.remove(2)
print(s1, '\n')
