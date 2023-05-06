# BFS
# 14502번. 연구소

from collections import deque

visit = [[0 for col in range(10)] for row in range(10)]     # BFS에서 바이러스 이동 칸을 표시하기 위한 배열
visit2 = [[0 for col in range(10)] for row in range(10)]    # 백트래킹에서 선택한 빈칸을 표시하기 위한 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    global answer

    for x in range(n):
        for y in range(m):
            visit[x][y] = lab[x][y]
            if(lab[x][y] == 2):
                queue.append([x, y])

    while(queue):
        x, y = queue.popleft()
        visit[x][y] = 1
        for i in range(4):
            # 이동할 칸이 n * m 범위 안이고, 연구실이 빈칸이고 방문하지 않은 칸이라면
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m and lab[x + dx[i]][y + dy[i]] == 0 and visit[x + dx[i]][y + dy[i]] == 0:
                queue.append([x + dx[i], y + dy[i]])
                visit[x + dx[i]][y + dy[i]] = 1

    cnt = 0     # 안전구역 저장
    for x in range(n):
        for y in range(m):
            if lab[x][y] == 0 and visit[x][y] == 0:
                cnt += 1
    answer = max(answer, cnt)

def backTraking(select):
    if select == 3:
        bfs()
        return
    for x in range(n):
        for y in range(m):
            # 연구소가 빈칸이고 해당 칸을 선택하지 않았다면
            if not lab[x][y] and not visit2[x][y]:
                visit2[x][y] = 1
                lab[x][y] = 1
                backTraking(select + 1)
                lab[x][y] = 0
                visit2[x][y] = 0


queue = deque()
answer = 0
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

backTraking(0)

print(answer)