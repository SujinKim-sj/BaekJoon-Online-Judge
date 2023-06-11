# 백준 단계별로 풀어보기 - 4. 1차원 배열
# 5597번. 과제 안 내신 분..?

n = [int(input()) for _ in range(28)]
for i in range(1, 31):
    if i not in n:
        print(i)