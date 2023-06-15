# 백준 단계별로 풀어보기 - 4. 1차원 배열
# 10811번. 바구니 뒤집기

n, m = map(int, input().split())

arr = [a for a in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    arr[i - 1: j] = reversed(arr[i - 1:j])

print(*arr)