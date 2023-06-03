# 삼성 SW 역량 테스트 기출 문제
# 백준 14501번. 퇴사

n = int(input())
t = []
p = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

dp = [0] * (n + 1)
money = 0

# 뒤에서 부터 시작
for i in range(n - 1, -1, -1):
    time = i + t[i]

    # time은 n보다 작아야함
    if time <= n:
        dp[i] = max(p[i] + dp[time], money)
        money = dp[i]
    else:
        dp[i] = money

print(money)



# 다른 사람의 풀이
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열 사용
dp = [0] * (N + 1)
for i in range(N):
    for j in range(i + L[i][0], N + 1):         # time이 n보다 작을 때까지만 for문 실행
        if dp[j] < L[i][1] + dp[i]:
            dp[j] = L[i][1] + dp[i]
print(max(dp))