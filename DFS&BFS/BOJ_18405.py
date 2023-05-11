# BFS
# 18405번. 경쟁적 전염

from collections import deque

# n : 크기, k : 바이러스 종류 수
n, k = map(int, input().split())

# 시험관과 바이러스 위치 입력 받기
graph = []  # 전체 보드 정보 담는 리스트
data = []   # 바이러스 정보 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 바이러스가 존재하면
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, x, y 삽입
            data.append((graph[i][j], 0, i, j))


# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

# 초, 바이러스 종류 확인할 위치 입력 받기
target_s, target_x, target_y = map(int, input().split())

# 상하좌우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 진행
while q:
    virus, s, x, y = q.popleft()

    # s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 바이러스 전염
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]

        # 해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

# s초 후 x,y에 위치한 바이러스 종류 출력
print(graph[target_x - 1][target_y - 1])