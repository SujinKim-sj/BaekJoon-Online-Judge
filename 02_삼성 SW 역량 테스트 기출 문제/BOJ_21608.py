# 삼성 SW 역량 테스트 기출 문제
# 백준 21608번. 상어 초등학교
# 구현

n = int(input())
students = [list(map(int, input().split())) for _ in range(n ** 2)]
classroom = [[0] * n for _ in range(n)] # 교실

# 상하좌우
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for i in range(n ** 2):
    st_num = students[i]
    tmp = [] # 선호 학생수, 빈칸 수, 좌표 담을 배열

    for r in range(n):
        for c in range(n):
            if classroom[r][c] == 0:
                like = 0
                blank = 0

                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < n and 0 <= nc < n:
                        if classroom[nr][nc] in st_num[1:]:
                            like += 1
                        if classroom[nr][nc] == 0:
                            blank += 1

                tmp.append([like, blank, r, c])
    tmp.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))

    # 정렬 후 가장 앞에 있는 리스트의 행과 열 번호에 학생 앉힘
    classroom[tmp[0][2]][tmp[0][3]] = st_num[0]

answer = 0
students.sort()

for r in range(n):
    for c in range(n):
        like = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if classroom[nr][nc] in students[classroom[r][c] - 1]:
                    like += 1
        if like != 0:
            answer += 10 ** (like - 1)


print(answer)