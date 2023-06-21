# 백준 단계별로 풀어보기 - 8. 일반 수학1
# 2745번. 진법 변환

n, b = input().split()
b = int(b)
answer = int(n, b)

print(answer)