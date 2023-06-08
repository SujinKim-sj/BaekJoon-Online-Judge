# 삼성 SW 역량 테스트 기출 문제
# 백준 14500번. 테트로미노
# 구현, 브루트포스 알고리즘

n, m = map(int, input().split())

# 방법 1) 테트로미노 모두 구해서 확인하기 - 단, pypy3으로 해야 시간초과가 나지 않음

# 테트로미노의 모든 경우의 수를 배열에 담는다
tetromino = [
    [[0, 0], [0, 1], [1, 0], [1, 1]],   # 1)
    [[0, 0], [0, 1], [0, 2], [0, 3]],   # 2)
    [[0, 0], [1, 0], [2, 0], [3, 0]],   # 3)
    [[0, 0], [0, 1], [0, 2], [-1, 2]],  # 4)
    [[0, 0], [1, 0], [2, 0], [2, 1]],   # 5)
    [[0, 0], [1, 0], [0, 1], [0, 2]],   # 6)
    [[0, 0], [0, 1], [1, 1], [2, 1]],   # 7)
    [[0, 0], [0, 1], [-1, 1], [-1, 2]], # 8)
    [[0, 0], [1, 0], [1, 1], [2, 1]],   # 9)
    [[0, 0], [0, 1], [0, 2], [-1, 1]],  # 10)
    [[0, 0], [1, 0], [2, 0], [1, 1]],   # 11)
    [[0, 0], [0, 1], [0, 2], [1, 1]],   # 12)
    [[0, 0], [0, 1], [-1, 1], [1, 1]],  # 13)
    [[0, 0], [0, 1], [1, 1], [1, 2]],   # 14)
    [[0, 0], [1, 0], [1, -1], [2, -1]], # 15)
    [[0, 0], [1, 0], [1, 1], [1, 2]],   # 16)
    [[0, 0], [0, 1], [1, 0], [2, 0]],   # 17)
    [[0, 0], [0, 1], [0, 2], [1, 2]],   # 18)
    [[0, 0], [1, 0], [2, 0], [2, -1]]  # 19)
]

paper = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for x in range(n):
    for y in range(m):
        for t in range(0, 19): # 테트로미노의 경우의 수 만큼
            sum = 0
            for i in range(4):
                nx = x + tetromino[t][i][0]
                ny = y + tetromino[t][i][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                sum += paper[nx][ny]
            answer = max(answer, sum)

print(answer)

# 방법2) 가장 시간이 적게 걸림

n, m = map(int,input().split())
graph = []
ans = 0

def shape1(i, j): # ㅡ
    if j+3 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i][j+3]

def shape2(i, j): # ㅣ
    if i+3 >= n:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+3][j]

def shape3(i, j): # L모양
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j+1]

def shape4(i, j): # L모양 대칭
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+2][j] + graph[i+2][j-1]

def shape5(i, j): # L모양 시계방향 회전
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i-1][j] + graph[i-1][j+1] + graph[i-1][j+2]

def shape6(i, j): # L대칭 시계방향 회전
    if i+1 >= n or j+2 >=m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+1][j+2]

def shape7(i, j): # L 시계방향 회전x2
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+2][j+1]

def shape8(i, j): # L대칭 시계방향 회전x2
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+2][j]

def shape9(i, j): # L 시계방향 회전x3
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i-1][j+2]

def shape10(i, j): # L대칭 시계방향 회전x3
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i][j+2] + graph[i+1][j+2]

def shape11(i, j): # ㅁ모양
    if i+1 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j] + graph[i+1][j+1]

def shape12(i, j): # 번개모양
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j+1]

def shape13(i, j): # 번개모양 회전
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i-1][j+1] + graph[i-1][j+2]

def shape14(i, j): #번개모양 대칭
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j-1]

def shape15(i, j): #번개모양 대칭 회전
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i+1][j+2]

def shape16(i, j): #ㅗ모양
    if i-1 < 0 or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i-1][j+1] + graph[i][j+2]

def shape17(i, j): #ㅗ모양 회전
    if i+2 >= n or j+1 >= m:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j+1] + graph[i+2][j]

def shape18(i, j): #ㅗ모양 회전x2
    if i+1 >= n or j+2 >= m:
        return 0
    return graph[i][j] + graph[i][j+1] + graph[i+1][j+1] + graph[i][j+2]

def shape19(i, j): #ㅗ모양 회전x3
    if i+2 >= n or j-1 < 0:
        return 0
    return graph[i][j] + graph[i+1][j] + graph[i+1][j-1] + graph[i+2][j]


for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        ans = max(ans, shape1(i,j), shape2(i,j), shape3(i,j), shape4(i,j), shape5(i,j), shape6(i,j), shape7(i,j), shape8(i,j), shape9(i,j),
                  shape10(i,j), shape11(i,j), shape12(i,j), shape13(i,j), shape14(i,j), shape15(i,j), shape16(i,j), shape17(i,j), shape18(i,j), shape19(i,j))

print(ans)


# 방법 3) dfs 사용 - 파이썬으로 하면 시간초과남
n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    board.append(list(map(int, input().split())))

answer = 0

def dfs(x, y, mysum, depth):
    global answer

    if depth == 3:
        answer = max(answer, mysum)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue

            if depth == 1:  # ㅗ 모양은 DFS로 만들 수 없으므로 예외처리
                visited[nx][ny] = True
                dfs(x, y, mysum + board[nx][ny], depth + 1)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, mysum + board[nx][ny], depth + 1)
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 0)
        visited[i][j] = False

print(answer)