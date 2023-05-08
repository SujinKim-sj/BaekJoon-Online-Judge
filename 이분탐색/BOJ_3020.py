# Binary Search
# 3020번. 개똥벌레

def upper_bound(s, e, d, L):
    # 찾고자하는 숫자 초과값이 처음 나오는 인덱스값 반환
    while e - s > 0:
        m = (s + e) // 2
        if L[m] <= d:
            s = m + 1
        else:
            e = m
    return e


def lower_bound(s, e, d, L):
    # 찾고자하는 숫자 이상의 값이 처음 나오는 인덱스값 반환
    while e - s > 0:
        m = (s + e) // 2
        if L[m] < d:
            s = m + 1
        else:
            e = m
    return e


up = []     # 동굴의 장애물 위 -> 아래 상태로 저장
down = []   # 동굴의 장애물 아래 -> 위 상태로 저장
result = [0] * 500001
n, h = map(int, input().split())
for i in range(n):
    obstacle = int(input())

    # 홀수번째 장애물은 up에 넣고 짝수번째 장애물은 down에 넣기
    if i % 2 == 1:
        up.append(obstacle)
    else:
        down.append(obstacle)

# 오름차순으로 정렬
up.sort()
down.sort()

answer = 0
mx = 2147483647     # 최솟값 찾기

for i in range(1, h + 1):
    idxd = lower_bound(0, len(down), i, down)       # 아래 -> 위  장애물을 처음 만나는 위치
    idxu = lower_bound(0, len(up), h - i + 1, up)   # 위 -> 아래  장애물을 처음 만나는 위치
    result[i] = n // 2 - idxd + n // 2 - idxu
    mx = min(mx, result[i])


for i in range(1, h + 1):
    if result[i] == mx:
        answer += 1

print(mx, answer)
