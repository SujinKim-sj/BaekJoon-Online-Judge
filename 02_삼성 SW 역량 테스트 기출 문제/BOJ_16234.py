# 삼성 SW 역량 테스트 기출 문제
# 백준 16234번. 인구 이동
# BFS

import sys
from collections import deque

N, L, R = map(int, input().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    temp = [] # 국경선을 공유하고 있는 나라들의 좌표값 넣을 배열
    queue.append((a, b))
    temp.append((a, b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # 국경선 열기
                if L <= abs(land[nx][ny] - land[x][y]) <= R:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    temp.append((nx, ny))

    return temp

result = 0 # 인구 이동이 필요한 날짜 수

while 1:
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    flag = 0 # 인구이동 시작시 1, 끝나면 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country = bfs(i, j)

                # 위의 조건에 의해 열어야하는 국경선이 모두 열렸으면 인구이동 시작
                if len(country) > 1:
                    flag = 1
                    # 연합을 이루고 있는 인구수 계산
                    number = sum(land[x][y] for x, y in country) // len(country)
                    for x, y in country:
                        land[x][y] = number

    # 연합 해체하고 모든 국경선 닫기
    if flag == 0:
        break
    result += 1 # while문 돌때마다 + 1(인구이동 한 횟수)


print(result)