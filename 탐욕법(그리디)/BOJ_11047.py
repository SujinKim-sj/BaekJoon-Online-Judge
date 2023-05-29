# 그리디 알고리즘
# 11047번 동전 0

n, k = map(int, input().split())
a = []

for i in range(n):
    a.append(int(input()))

count = 0
for i in reversed(range(n)):
    count += k // a[i]
    k = k % a[i]

print(count)