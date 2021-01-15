result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)


word1 = "ABC"
word2 = "CDF"
result = [i+j for i in word1 for j in word2]
print(result)

result = [i+j for i in word1 for j in word2 if not i==j]
print(result)

result = [[i+j for i in word1 ] for j in word2]
print(result)


# 이중 리스트
words = 'apple banana computer doctor eraser fox grape'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)


