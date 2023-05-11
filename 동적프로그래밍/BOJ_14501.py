# DP, 완전탐색
# 14501번. 퇴사

# 퇴사까지 남은 날짜
n = int(input())
t = []  # 기간
p = []  # 금액
dp = [0] * (n + 1)  # dp 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 거꾸로 뒤에서 부터 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i

    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)