# 백준 단계별로 풀어보기 - 7. 2차원 배열
# 10798번. 세로읽기

arr = [input() for _ in range(5)]

for i in range(15): # 최대 15글자이므로
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end="")