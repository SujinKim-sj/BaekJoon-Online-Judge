# Greedy
# 1931번. 회의실 배정

N = int(input())
meet = []

# 회의실 상태 입력받기
for i in range(N):
    A, B = map(int, input().split())
    meet.append([A, B])

# 회의가 끝나는 시간이 빠른 순으로, 끝나는 시간이 같다면 회의 시작 시간이 빠른 순으로 리스트 정렬
meet.sort(key=lambda x: (x[1], x[0]))

answer = 0
endTime = 0

# 회의가 끝난 시간보다 시작 시간이 크다면 answer += 1,
# 회의가 끝난 시간을 시작 시간에 해당하는 회의가 끝난 시간 값으로 바꿈
for i in range(len(meet)):
    if endTime <= meet[i][0]:
        endTime = meet[i][1]
        answer += 1

print(answer)