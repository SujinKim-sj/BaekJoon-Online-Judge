from collections import deque
def right(idx, d): # 오른쪽 톱니바퀴 확인
    # 마지막 톱니는 확인 안함
    if idx > 3:
        return
    # 같은 극이 아니면 회전
    if sawtooth[idx - 1][2] != sawtooth[idx][6]:
        right(idx + 1, -d)
        sawtooth[idx].rotate(d)


def left(idx, d):
    # 첫번째 톱니는 확인하지 않음
    if idx < 0:
        return
    # 같은 극이 아니면 회전
    if sawtooth[idx][2] != sawtooth[idx + 1][6]:
        left(idx - 1, -d)
        sawtooth[idx].rotate(d)


# 톱니바퀴 4개 입력받기
sawtooth = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())   # 회전 횟수

for _ in range(k):
    # 회전 정보(회전 톱니 번호 인덱스, 회전 방향) 입력받기
    idx, d = map(int, input().split())
    idx -= 1
    # 회전할 톱니 번호의 시계방향, 반시계방향이 회전 가능한지 확인하고 회전한다
    # -d인 이유는 회전할 톱니번호가 회전하는 방향의 반대방향으로 회전해야 하기 때문
    left(idx - 1, -d)
    right(idx + 1, -d)

    # 회전할 톱니 번호의 톱니도 회전
    sawtooth[idx].rotate(d)


# 점수 계산하여 출력
score = 0
for i in range(4):
    if sawtooth[i][0] == 1:
        score += 2 ** i

print(score)