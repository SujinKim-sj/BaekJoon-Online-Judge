# 백준 단계별로 풀어보기 - 4. 1차원 배열
# 10813번. 공 바꾸기

n, m = map(int, input().split())

arr = [a + 1 for a in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = arr[i - 1]
    arr[i - 1] = arr[j - 1]
    arr[j - 1] = tmp

for i in range(n):
    print(arr[i], end=" ")
