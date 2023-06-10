# 삼성 SW 역량 테스트 기출 문제
# 백준 20056번. 마법사 상어와 파이어볼
# 구현, 시뮬레이션

N, M, K = map(int, input().split())

board = [[[] for _ in range(N)] for _ in range(N)]

# direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 8가지 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

# r, c, m, s, d 입력 받아서 파이어볼의 위치(r, c)에 원소 삽입
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r - 1][c - 1].append([m, s, d])



def move():
    b = [[[] for _ in range(N)] for _ in range(N)]

    # 1. 자신의 방향 d로 속력 s칸 만큼 이동
    for i in range(N):
        for j in range(N):
            # 파이어볼이 없는 위치이면
            if len(board[i][j]) == 0:
                continue
            # 방향 d로 속력 s칸 만큼 이동
            for info in board[i][j]:
                x, y = i, j
                m, s, d = info
                nx = (x + dx[d] * s) % N
                ny = (y + dy[d] * s) % N
                b[nx][ny].append([m, s, d])

    # 2.이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다
    for i in range(N):
        for j in range(N):
            if len(b[i][j]) <= 1:
                continue
            m_sum, s_sum, a_odd, a_even = 0, 0, True, True
            cnt = len(b[i][j])

            for info in b[i][j]:
                m, s, d = info
                m_sum += m
                s_sum += s

                # 홀수
                if d % 2 == 1:
                    a_even = False
                else:
                    a_odd = False
            b[i][j] = []

            if m_sum < 5:
                continue
            else:
                # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
                if a_odd or a_even:
                    for info in [0, 2, 4, 6]:
                        b[i][j].append([m_sum // 5, s_sum // cnt, info])
                else:
                    for info in [1, 3, 5, 7]:
                        b[i][j].append([m_sum // 5, s_sum // cnt, info])

    # board에 b에 담아놓았던 파이어볼 정보 담기
    for i in range(N):
        for j in range(N):
            board[i][j] = b[i][j]



# K번 이동 명령 후, 남아있는 파이어볼 질량의 합 출력
for _ in range(K):
    move()

answer = 0

for i in range(N):
    for j in range(N):
        for b in board[i][j]:
            answer += b[0]

print(answer)