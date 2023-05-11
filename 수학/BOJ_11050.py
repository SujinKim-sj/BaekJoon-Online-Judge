# 조합론
# 11050번. 이항 계수 1

n, k = list(map(int, input().split()))

# n!
up = 1
for i in range(1, n + 1):
    up *= i

# (n - k)!
down = 1
for i in range(1, n - k + 1):
    down *= i

# k!
down2 = 1
for i in range(1, k + 1):
    down *= i

down *= down2

print(up // down)