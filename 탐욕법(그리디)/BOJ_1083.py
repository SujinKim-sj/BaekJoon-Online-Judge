# Greedy
# 1083번. 소트

N = int(input())
arr = [int(i) for i in input().split()]

s = int(input())
while True:
    tof = False
    # i의 위치 기준으로 오른쪽에 있는 수 중 남은 S번 교체해서 바꿀 수 있는 최댓값의 위치 저장
    for i in range(N):
        idx = i
        cmp = 0
        for j in range(N - 1, i, -1):
            if arr[idx] < arr[j] and j - i <= s:
                idx = j
                tof = True
                cmp = j - i
        if idx != i:
            tmp = arr[idx]
            del arr[idx]
            arr.insert(i, tmp)
            s -= cmp
            break
    if tof == False:
        break

print(*arr)