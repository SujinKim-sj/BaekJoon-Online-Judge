# Back Traking
# 15649번. N과 M(1)

n, m = map(int, input().split())
answer = []

# 백트래킹 알고리즘을 위한 재귀함수
def backTraking(depth):
    if depth == m:      # depth는 수열의 길이
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n + 1):
        if i in answer:         # 추가 : 같은 값이 있으면 지나감
            continue
        answer.append(i)
        backTraking(depth + 1)
        answer.pop()

backTraking(0)