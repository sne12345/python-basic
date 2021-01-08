wintable = {
    '가위' : '보',
    '바위' : '가위',
    '보' : '바위',
}

print(wintable['가위'])

for i in wintable.items():
    print("{}는 {}를 이긴다.".format(i[0], i[1]))


