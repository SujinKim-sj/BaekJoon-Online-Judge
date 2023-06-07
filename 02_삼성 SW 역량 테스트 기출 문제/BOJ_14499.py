# 삼성 SW 역량 테스트 기출 문제
# 백준 14499번. 주사위 굴리기
# 구현, 시뮬레이션

n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0] # 주사위 초기화
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위 굴리기
def turn_dice(direction):
    global dice
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 1: # 동쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif direction == 2: # 서쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif direction == 3: # 북쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    else: # 남쪽
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


# 이동하는 명령
for i in order:
    idx = i - 1
    nx = x + dx[idx]
    ny = y + dy[idx]

    # 지도 내의 범위이면
    if 0 <= nx < n and 0 <= ny < m:
        turn_dice(i) # 주사위 굴리기

        # 이동한 칸에 쓰여있는 수가 0이면, 주사위 바닥면에 쓰여있는 수가 복사
        if arr[nx][ny] == 0:
            arr[nx][ny] = dice[5]
        else: # 0이 아니면, 칸에 쓰인 수가 주사위의 바닥면으로 복사, 칸의 수는 0이 됨
            dice[5] = arr[nx][ny]
            arr[nx][ny] = 0
    else: # 지도를 벗어나면 명령 무시
        continue

    x, y = nx, ny   # x와 y 값을 갱신해줘야 한다
    print(dice[0])  # 주사위의 맨 위의 숫자 출력