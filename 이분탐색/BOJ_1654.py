# Binary Search
# 1654번. 랜선 자르기

k, n = map(int, input().split())
lanson = []
for i in range(k):
    lanson.append(int(input()))

start, end = 0, 10000000000
answer = 0

while start <= end:
    mid = (start + end) // 2
    num = 0
    for len in lanson:
        num += len // mid
    if num >= n:
        start = mid + 1
        if mid > answer:
            answer = mid
    else:
        end = mid - 1

print(answer)