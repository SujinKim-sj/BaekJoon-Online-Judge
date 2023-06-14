# 백준 단계별로 풀어보기 - 4. 1차원 배열
# 10810번. 공 넣기

# 바구니 개수, 공 넣는 횟수 입력 받기
n, m = map(int, input().split())

basket = [[] for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())

    for idx in range(i - 1, j):
        if len(basket[idx]) == 0:
            basket[idx].append(k)
        else:
            basket[idx].pop()
            basket[idx].append(k)


for idx in range(n):
    if len(basket[idx]) == 0:
        print(0, end=" ")
    else:
        print(basket[idx][0], end=" ")