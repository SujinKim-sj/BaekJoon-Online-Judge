# 백준 단계별로 풀어보기 - 7. 2차원 배열
# 2566번. 최댓값

arr = [list(map(int, input().split())) for _ in range(9)]

maxArr = 0

for i in range(9):
    for j in range(9):
        maxArr = max(maxArr, arr[i][j])


for i in range(9):
    for j in range(9):
        if arr[i][j] == maxArr:
            print(maxArr)
            print(i + 1, j + 1)
            break


# 다른 사람의 풀이
max = max(arr)
max_index = arr.index(max)

print(max)
print(max_index // 9 + 1, max_index % 9 + 1)