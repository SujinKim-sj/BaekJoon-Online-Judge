# 백준 단계별로 풀어보기 - 7. 2차원 배열
# 2563번. 색종이

n = int(input())
paper = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = list(map(int, input().split()))

    for i in range(x, x + 10):
        for j in range(y, y + 10):
           paper[i][j] = 1

answer = 0
for i in paper:
    answer += sum(i)

print(answer)