# 백준 단계별로 풀어보기 - 8. 일반 수학1
# 2292번. 벌집

n = int(input())
answer = 1
comb = 1

while n > comb:
    comb += answer * 6
    answer += 1

print(answer)