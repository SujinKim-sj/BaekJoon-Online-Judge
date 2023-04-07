# Queue
# 3190번. 뱀

from collections import deque


def direction_change(d, c):
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


N = int(input())    # 보드의 크기
K = int(input())    # 사과의 개수
board = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

L = int(input())    # 뱀 방향 전환 횟수
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

direction = 1   # 뱀의 이동 방향 (오른쪽)
time = 1        # 게임이 진행된 시간
y, x = 0, 0     # 뱀 머리의 현재 위치 저장하는 변수
snake = deque([[y, x]])
board[y][x] = 2     # 뱀이 존재하는 곳은 2로 설정

while True:
    y, x = y + dy[direction], x + dx[direction]
    if 0 <= y < N and 0 <= x < N and board[y][x] != 2:
        if not board[y][x] == 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        board[y][x] = 2
        snake.append([y, x])

        if time in times.keys():
            direction = direction_change(direction, times[time])
        time += 1
    else:
        break

print(time)  # 몇 초 걸리는지 출력
