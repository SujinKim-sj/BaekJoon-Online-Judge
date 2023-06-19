# 백준 단계별로 풀어보기 - 7. 2차원 배열
# 2738번. 행렬 덧셈

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

newArr = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        newArr[i][j] = a[i][j] + b[i][j]


for i in newArr:
    print(' '.join(map(str, i)))