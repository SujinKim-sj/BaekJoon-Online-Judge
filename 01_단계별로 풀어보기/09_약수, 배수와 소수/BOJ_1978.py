# 백준 단계별로 풀어보기 - 9. 약수, 배수와 소수
# 1978번. 소수 찾기

n = int(input())
answer = 0
arr = list(map(int, input().split()))

for i in range(n):
    cnt = 0
    for j in range(1, arr[i] + 1):
        if arr[i] % j == 0:
            cnt += 1
    if cnt == 2:
        answer += 1

print(answer)