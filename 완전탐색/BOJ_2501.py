# Brute Force
# 2501번. 약수 구하기

n, k = list(map(int, input().split()))

arr = []

for i in range(1, n + 1):
    if n % i == 0:
        arr.append(i)

if len(arr) < k :
    print(0)
else:
    print(arr[k - 1])

