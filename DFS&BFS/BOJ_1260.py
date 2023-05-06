# DFS, BFS
# 1260번. DFS와 BFS

from collections import deque

N, M, V = map(int, input().split())
vertex = [[0] * (N + 1) for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    vertex[a][b] = vertex[b][a] = 1

# 재방문하지 않도록 visit 배열을 생성한다(전부 0으로 초기화)
visit = [0] * (N + 1)


def dfs(V):
    visit[V] = 1
    # 방문한 정점 출력
    print(V, end=' ')
    for i in range(1, N + 1):
        if visit[i] == 0 and vertex[V][i] == 1:
            dfs(i)


def bfs(V):
    visit[V] = 0
    queue = deque()
    queue.append(V)

    while queue:
        V = queue.popleft()
        print(V, end=' ')

        for i in range(1, N + 1):
            # dfs에서 visit을 이미 1로 다 바꿔놓았기 때문에
            # 이번에는 visit[정점] = 0이면 방문한 정점, 1이면 방문하지 않은 정점
            if visit[i] == 1 and vertex[V][i] == 1:
                queue.append(i)
                visit[i] = 0


dfs(V)
print()
bfs(V)