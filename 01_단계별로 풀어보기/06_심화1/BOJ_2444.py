# 백준 단계별로 풀어보기 - 6. 심화 1
# 2444번. 별 찍기 7

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))