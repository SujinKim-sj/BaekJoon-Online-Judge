# 백준 단계별로 풀어보기 - 8. 일반 수학1
# 2869번. 달팽이는 올라가고 싶다

a, b, v = map(int, input().split())
loc = (v - b) % (a - b)

if loc == 0:
    answer = (v - b) // (a - b)
else:
    answer = (v - b) // (a - b) + 1

print(answer)

# 방법 2
# print((v - b - 1) // (a - b) + 1)

# 틀린 방법
# 반복문 사용하면 시간 초과남
# answer = 0  # 올라가는데 걸리는 시간(날짜)
# while loc < v:
#     answer += 1
#     loc += a
#     if loc == v:
#         break
#     else:
#         loc -= b
#
# print(answer)