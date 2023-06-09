# 삼성 SW 역량 테스트 기출 문제
# 백준 17144번. 미세먼지 안녕!
# 구현, 시뮬레이션

r, c, t = map(int, input().split())
house = [list(map(int, input().split())) for i in range(r)]

up = -1
down = -1

# 공기청정기 위치 찾기
for i in range(r):
    # 0인 이유는 공기청정기는 항상 1번열에 설치되어있기 때문
    if house[i][0] == -1:
        up = i
        down = i + 1
        break

# 미세먼지 확산
def spread():
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]

    # 확산된 미세먼지 양을 담을 배열
    h = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if house[x][y] != 0 and house[x][y] != -1:
                cnt = 0     # 확산된 방향의 개수
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 범위를 벗어나는 경우 혹은 공기청정기가 있는 경우엔 확산이 일어나지 않음
                    if nx < 0 or nx >= r or ny < 0 or ny >= c or house[nx][ny] == -1:
                        continue
                    else:
                        h[nx][ny] += house[x][y] // 5
                        cnt += 1
                h[x][y] += (house[x][y] - (house[x][y] // 5) * cnt)

    # 확산 후 미세먼지 양을 반영해준다
    for i in range(r):
        for j in range(c):
            if house[i][j] != -1:
                house[i][j] = h[i][j]


# 공기청정기 윗부분
def clean_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    i = 0
    before = 0
    x, y = up, 1    # 공기청정기 옆 부터 시작하므로 y는 1로 설정함

    while True:
        nx = x + dx[i]
        ny = y + dy[i]

        if x == up and y == 0:  # 공기청정기 위치와 같으면
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:  # 범위 벗어나면 방향 바꿔줌
            i += 1
            continue

        # 바람불면 방향대로 한칸씩 이동
        house[x][y], before = before, house[x][y]
        x, y = nx, ny


def clean_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    i = 0
    before = 0
    x, y = down, 1

    while True:
        nx = x + dx[i]
        ny = y + dy[i]

        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            i += 1
            continue
        house[x][y], before = before, house[x][y]
        x, y = nx, ny



#t초 후 결과
for i in range(t):
    # 미세먼지 확산
    spread()

    # 공기청정기 작동
    clean_up()
    clean_down()

# t초 후 남아있는 미세먼지의 양 총합 출력
# 공기청정기 값 빼줘야하므로 2로 설정
answer = 2
for i in range(r):
    for j in range(c):
        answer += house[i][j]

print(answer)