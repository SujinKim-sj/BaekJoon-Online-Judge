# 삼성 SW 역량 테스트 기출 문제
# 백준 15868번. 치킨 배달

import sys
from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

house = []
chicken = []

# 집과 치킨집의 좌표를 리스트에 저장
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
           house.append([i, j])
        elif city[i][j] == 2:
           chicken.append([i, j])


# 방법1) 백트래킹으로 풀기
# depth: 고른 치킨집 수, i: 고른 치킨집 번호
def back(depth, i):
  global result
  chicken_total_dist = 0
  # 치킨집 m개를 골랐다면 치킨 거리 계산
  if depth == m:
    for h in house:
      chicken_dist = int(1e9)
      for c in select:
        chicken_dist = min(chicken_dist, abs(h[0]-c[0]) + abs(h[1]-c[1]))
      chicken_total_dist += chicken_dist
    result = min(chicken_total_dist,result)
    return
	# 고른 치킨 집을 제외하고 back
  for idx in range(i, K):
    select.append(chicken[idx])
    back(depth+1, idx+1)
    select.pop()

select = []

K = len(chicken)      # 총 치킨집 수
result = int(1e9)

# 조합 시작
for t in range(K):
  back(0, t)

print(result)

# 방법2) 조합으로 풀기
# m개의 치킨집 선택
result = sys.maxsize
for c in combinations(chicken, m):
    temp = 0
    for h in house:
        distance = sys.maxsize
        for i in range(m):
            # 치킨 거리 구하기
            distance = min(distance, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        temp += distance
    result = min(result, temp)

print(result)
