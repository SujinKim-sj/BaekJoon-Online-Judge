# 삼성 SW 역량 테스트 기출 문제
# 백준 3190번. 뱀
# 구현, 시뮬레이션, 자료구조, 덱, 큐

from collections import deque

n = int(input())    # 보드 크기
k = int(input())    # 사과 개수

graph = [[0] * (n) for _ in range(n)]     # 그래프 생성

# 사과 위치 입력받고 사과 위치 표시
for i in range(k):
    a1, a2 = map(int, input().split())
    graph[a1 - 1][a2 - 1] = 1     # 사과 위치 표시

l = int(input())    # 뱀의 방향 변환 횟수
info = {}           # 뱀의 방향 변환 정보
for _ in range(l):
    s, c = input().split()
    info[int(s)] = c

count = 0                   # 초 카운트 시작
snake = deque([(0, 0)])     # 뱀 위치 시작은 1행 1열 부터
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0
graph[x][y] = 2             # 뱀 위치 시작
i = 0

while True:
    nx = x + dx[i]
    ny = y + dy[i]

    # 뱀이 벽이나 자기자신의 몸과 부딪히면 종료
    if nx >= n or nx < 0 or ny >= n or ny < 0 or (nx, ny) in snake:
        count += 1
        break

    if graph[nx][ny] == 1:  # 사과가 있을 때
        graph[nx][ny] = 2
        snake.append((nx, ny))
    elif graph[nx][ny] == 0:
        snake.append((nx, ny))
        graph[nx][ny] = 2
        a, b = snake.popleft()
        graph[a][b] = 0

    x, y = nx, ny   # 값 갱신
    count += 1

    if count in info.keys():
        if info[count] == 'L':
            i = (i - 1) % 4
        elif info[count] == 'D':
            i = (i + 1) % 4



print(count)