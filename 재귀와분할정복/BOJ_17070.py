# 재귀
# 17070번. 파이프 옮기기 1

def recursive(y, x, shape):
    global ans
    if y > n or x > n:
        return
    if y == n and x == n:
        ans += 1
    if home[y][x + 1] == 0 and (shape == 0 or shape == 2):
        recursive(y, x + 1, 0)
    if home[y + 1][x] == 0 and (shape == 1 or shape == 2):
        recursive(y + 1, x, 1)
    if home[y + 1][x] == 0 and home[y][x + 1] == 0 and home[y + 1][x + 1] == 0:
        recursive(y + 1, x + 1, 2)


# 집의 크기 입력받기
n = int(input())
home = [[0 for col in range(18)] for row in range(18)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        home[i][j] = row[j - 1]

ans = 0
recursive(1, 2, 0)
print(ans)