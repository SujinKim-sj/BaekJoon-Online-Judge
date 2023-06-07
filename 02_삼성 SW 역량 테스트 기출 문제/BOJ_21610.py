# 삼성 SW 역량 테스트 기출 문제
# 백준 21610번. 마법사 상어와 비바라기
# 구현, 시뮬레이션

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]      # 격자 입력 받기
order = [list(map(int, input().split())) for _ in range(m)]  # 명령(이동 방향, 칸 수)

# 8가지 방향
dir_x = [0, -1, -1, -1, 0, 1, 1, 1]
dir_y = [-1, -1, 0, 1, 1, 1, 0, -1]

cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]    # 초기 구름 상태

for d, s in order:
    for i in range(len(cloud)):
        x = (cloud[i][0] + (s * dir_x[d - 1])) % n
        y = (cloud[i][1] + (s * dir_y[d - 1])) % n

        # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다
        a[x][y] += 1

        # 구름 이동
        cloud[i] = [x, y]

    # 대각선 방향(dir_x dir_y 의 1, 3, 5, 7번째 방향) 물 복사
    for x, y in cloud:
        for i in range(1, 8, 2):
            nx = x + dir_x[i]
            ny = y + dir_y[i]

            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] != 0:
                    a[x][y] += 1    # 물이 있는 바구니 수 만큼 물의 양 증가시킴

        a[x][y] *= -1 # 구름이 사라진 칸인지 체크하기 위한 음수 처리

    # 구름이 모두 사라진다
    cloud.clear()

    # 구름이 있었던 칸을 제외한 나머지 칸 중에서 물의 양이 2이상인 칸에 구름 생성
    for i in range(n):
        for j in range(n):
            if a[i][j] >= 2:
                cloud.append([i, j])
                a[i][j] -= 2    # 물의 양은 2만큼 감소
            elif a[i][j] < 0:   # 구름이 사라진 칸은 제외하고 구름 생성
                # 다시 양수로 만들어 줌
                a[i][j] *= -1

# 명령 for문 종료

# 바구니에 들어있는 물의 양의 합
answer = 0
for i in range(n):
    for j in range(n):
        answer += a[i][j]

print(answer)