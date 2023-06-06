# 삼성 SW 역량 테스트 기출 문제
# 백준 20055번. 컨베이어 벨트 위의 로봇

from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([False] * n)

answer = 0 # 단계 횟수 카운트
while True:
    answer += 1

    # 1)벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.rotate(1)
    robot.rotate(1)

    # 로봇이 내리는 위치에 도달하면 즉시 내린다
    robot[n - 1] = False

    # 2)가장 먼저 벨트에 올라간 로봇부터(n-2번째 위치에 존재), 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다
    for i in range(n - 2, -1, -1):
        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다
        if robot[i] == True and robot[i + 1] == False and belt[i + 1] >= 1:
            robot[i], robot[i + 1] = False, True
            belt[i + 1] -= 1

    # 로봇이 내리는 위치에 도달하면 즉시 내린다
    robot[n - 1] = False

    # 3)올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
    if belt[i] > 0:
        robot[i] = True
        belt[i] -= 1

    # 4)내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다
    if belt.count(0) >= k:
        break

print(answer)