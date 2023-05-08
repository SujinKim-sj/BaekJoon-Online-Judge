# Binary Search
# 1920번. 수 찾기

n = int(input())
a = list(map(int, input().split()))
a.sort() # 오름차순으로 정렬


def binarySearch(target):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            print(1)
            return
        elif a[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1
    print(0)    # 못찾았을 경우 출력
    return


m = int(input())
b = list(map(int, input().split()))
for i in range(m):
    binarySearch(b[i])