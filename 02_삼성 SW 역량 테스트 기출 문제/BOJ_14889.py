# 02_삼성 SW 역량 테스트 기출 문제
# 백준 14889번. 스타트와 링크
from itertools import combinations

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 나의 풀이 - 1) 조합 사용
# 1, 2 / 3, 4 로 나뉘면 1,2 + 2,1 이랑 3,4 + 4,3 값 비교해서 둘이 뺀 값을 배열에 넣어준다
# 배열 중 최솟값 반환하면 정답 min()

members = list(range(n)) # 전체 멤버를 포함하는 리스트 생성
result = [] # start - link 값을 담을 배열

for s in combinations(members, n // 2):
    start, link = 0, 0
    l = list(set(members) - set(s))
    for i in combinations(s, 2): # 스타트팀
        start += arr[i[0]][i[1]]
        start += arr[i[1]][i[0]]
    for j in combinations(l, 2): # 링크팀
        link += arr[j[0]][j[1]]
        link += arr[j[1]][j[0]]
    # 능력치 차 구하기
    if start > link:
        result.append(start - link)
    else:
        result.append(link - start)


# 능력치 차 중 최솟값 출력
print(min(result))


#### 다른 사람의 풀이
# 2) 백트래킹
def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    power1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += graph[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

visited = [False for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]
min_diff = int(1e9)

dfs(0, 0)
print(min_diff)


# 3) zip() 함수 이용
from sys import stdin
from itertools import combinations

n = int(stdin.readline())
s = [list(map(int, stdin.readline().split())) for _ in range(n)]

member_stat = [sum(i) + sum(j) for i, j in zip(s, zip(*s))]
total_stat = sum(member_stat) // 2

res = 1e9
for c in combinations(member_stat[:-1], n // 2):
    res = min(res, abs(total_stat - sum(c)))

print(res)