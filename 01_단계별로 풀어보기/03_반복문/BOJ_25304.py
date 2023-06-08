# 단계별로 풀어보기 - 3.반복문
# 백준 25304번. 영수증

x = int(input())
n = int(input())

sum = 0
for i in range(n):
    a, b = map(int, input().split())
    sum += a * b

if sum == x:
    print("Yes")
else:
    print("No")