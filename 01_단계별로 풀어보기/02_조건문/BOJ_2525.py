# 단계별로 풀어보기 - 2.조건문
# 백준 2525번. 오븐 시계
a, b = map(int, input().split())
cook = int(input())

if cook >= 60:
    a += cook // 60
    b += cook % 60
else:
    b += cook

if b >= 60:
    a += b // 60
    b %= 60

if a >= 24:
    a = a - 24

print(a, b)