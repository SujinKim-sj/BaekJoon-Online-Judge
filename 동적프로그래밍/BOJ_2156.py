# Dynamic Programming
# 2156번. 포도주 시식

dp = [0] * 10001
glass = [0] * 10001     # 포도주

n = int(input())
for i in range(1, n + 1):
    glass[i] = int(input())

dp[1] = glass[1]    # 첫 번째 포도주 잔으로 설정
dp[2] = glass[1] + glass[2]     # 첫 번째 + 두 번째 포도잔으로 설정

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + glass[i], dp[i - 3] + glass[i - 1] + glass[i])

print(dp[n])