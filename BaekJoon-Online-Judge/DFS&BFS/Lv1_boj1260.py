# 1260번 - DFS와 BFS

def dfs(v):
    # 방문한 곳은 1
    visited[v] = 1
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visited[v] = 0
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 0

# n = 정점의 개수
# m = 간선의 개수
# v = 시작 정점의 번호
n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for i in range(n + 1)]

visited = [0] * (n + 1)

for i in range(m):
    i, j = map(int, input().split())
    graph[i][j] = graph[j][i] = 1

dfs(v)
print()
bfs(v)
