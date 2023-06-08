# 단계별로 풀어보기 - 3.반복문
# 백준 25314번. 코딩은 체육과목 입니다

n = int(input())

for i in range(n // 4):
    if i == n // 4 - 1:
        print("long ", end="int")
    else:
        print("long", end=" ")