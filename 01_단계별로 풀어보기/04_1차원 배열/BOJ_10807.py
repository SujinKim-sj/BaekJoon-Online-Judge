# 백준 단계별로 풀어보기 - 4. 1차원 배열
# 10807번. 개수 세기

n = int(input())
arr = list(map(int, input().split()))
v = int(input())

print(arr.count(v))