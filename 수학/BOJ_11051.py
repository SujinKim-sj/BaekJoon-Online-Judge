# 조합론
# 11051번. 이항 계수 2

n, k = map(int, input().split())
dp = [[0] * 1001 for _ in range(1001)]

for i in range(1, n + 1):
    for j in range(0, i + 1):
        # k가 0이라면 nCk의 값은 전부 1이된다
        if j == 0:
            dp[i][j] = 1
        elif j == i:    # k가 n 값과 같다면 전부 1이된다
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10007


print(dp[n][k])