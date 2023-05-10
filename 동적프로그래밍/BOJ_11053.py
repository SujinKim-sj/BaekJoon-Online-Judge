# Dynamic Programming
# 11053번. 가장 긴 증가하는 부분 수열

dp = [0] * 1001     # dp 메모이제이션을 위한 배열 크기를 n의 최댓값 + 1로 설정

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

answer = 0
for i in range(1, n + 1):
    for j in range(0, i):
        # 점화식
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    answer = max(answer, dp[i])

print(answer)