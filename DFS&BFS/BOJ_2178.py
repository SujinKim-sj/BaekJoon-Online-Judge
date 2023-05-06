# BFS
# 2178번. 미로 탐색

from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
q.append((0, 0))

def bfs():
    while q:
        x, y = q.popleft()  # 큐에서 가장 먼저 삽입된 x, y 위치를 꺼낸다

        for k in range(len(d)):
            dx = x + d[k][0]
            dy = y + d[k][1]
            # print('dx, dy:', dx, dy)
            if 0 <= dx < N and 0 <= dy < M:
                if maze[dx][dy] == 1:
                    # 현재 정점에서 가장가까운 dx, dy의 위치값을 [현재 정점 + 1]로 바꿔준다
                    maze[dx][dy] = maze[x][y] + 1
                    # print('maze', maze[dx][dy])
                    q.append((dx, dy))

maze[0][0] = 1
bfs()
print(maze[N - 1][M - 1])