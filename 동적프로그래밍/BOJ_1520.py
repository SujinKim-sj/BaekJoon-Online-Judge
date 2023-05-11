# Dynamic Programming
# 1520번. 내리막 길

m, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]       # 방문한 좌표를 다시 방문하지 않기 위해 설정
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]   # 상하좌우 이동


def dp_bruteForce(y, x):
    # -1이 아니면 방문한 점이므로 반환
    if dp[y][x] != -1:
        return dp[y][x]

    # m-1, n-1에 도달했다면 1을 반환
    if y == m - 1 and x == n - 1:
        return 1

    # 방문했음을 표시
    dp[y][x] = 0

    # 현재 좌표에 dp값들을 계속 더해줌
    for i in range(0, 4):
        dy = y + move[i][0]
        dx = x + move[i][1]

        if 0 <= dy < m and 0 <= dx < n and map[y][x] > map[dy][dx]:
            dp[y][x] += dp_bruteForce(dy, dx)

    return dp[y][x]


print(dp_bruteForce(0, 0))