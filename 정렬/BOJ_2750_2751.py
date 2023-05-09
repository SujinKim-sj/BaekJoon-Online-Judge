# Sort
# 2750번, 2751번. 수 정렬하기
import sys

n = int(input())
# a = [int(input()) for _ in range(n)]
arr = list()
for i in range(n):
    arr.append(int(sys.stdin.readline()))   # 시간 단축을 위해 입력받기

# 1. 선택 정렬
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

# 2. 퀵 정렬 이상의 효율적인 시간복잡도 정렬
arr.sort()

for i in arr:
    print(i)