# 최단경로, 플로이드 워셜, dp
# 11404번. 플로이드
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

# 2차원 배열 초기화
adj = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            adj[a][b] = 0

# 간선에 대한 정보를 입력받아 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    if c < adj[a][b]:
        adj[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            adj[a][b] = min(adj[a][b], adj[a][k] + adj[k][b])

# 수행된 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if adj[i][j] == INF:
            print(0, end=" ")
        else:
            print(adj[i][j], end=" ")
    print()
