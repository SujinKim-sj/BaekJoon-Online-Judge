# DFS
# 1182번. 부분수열의 합

def dfs(idx, sum):
    global answer
    if idx >= n:
        return
    sum += sArr[idx]

    if sum == s:
        answer += 1

    # 현재 정점의 수열을 택하지 않고 현재 정점과 연결된 다음 위치의 정점 idx + 1로 이동
    dfs(idx + 1, sum - sArr[idx])
    # 현재 정점의 수열을 택하고 현재 정점과 연결된 다음 위치의 정점 idx + 1로 이동
    dfs(idx + 1, sum)


n, s = map(int, input().split())
sArr = list(map(int, input().split()))

answer = 0  # 부분 수열의 개수
dfs(0, 0)
print(answer)