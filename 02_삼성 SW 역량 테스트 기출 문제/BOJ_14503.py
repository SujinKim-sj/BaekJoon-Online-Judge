# 삼성 SW 역량 테스트 기출 문제
# 백준 14503번. 로봇 청소기

n, m = map(int, input().split())

# d -> 0:북 / 1:동 / 2:남 / 3:서
r, c, d = map(int, input().split())

# 방의 칸, 벽 정보 입력받기
room = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 로봇청소기 방문여부 정보 넣을 배열
visited = [[0] * m for _ in range(n)]
cnt = 1     # 청소한 칸 개수

# 1) 현재 칸이 청소되지 않은 경우, 현재 칸을 청소한다
visited[r][c] = 1       # 방문 표시

# 2)
while True:
    flag = 0                # 청소여부 표시

    # 상하좌우로 청소 시작
    for i in range(4):
        d = (d + 3) % 4     # 반시계방향으로 90도 회전
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r, c = nx, ny          # 현재 위치 갱신
                flag = 1        # 청소 했다고 표시
                break

    # 청소가 4방향 모두 되어 있을 때
    if flag == 0:
        # 후진했을 때, 벽이 아니라 빈칸이면 후진한 위치로 갱신
        if room[r - dx[d]][c - dy[d]] == 1:
            print(cnt)  # 청소한 칸 개수 출력
            break
        else:   # 벽이면 작동 멈춤
            r = r - dx[d]
            c = c - dy[d]