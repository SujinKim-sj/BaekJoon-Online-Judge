# 백준 단계별로 풀어보기 - 6. 심화 1
# 10988번. 팰린드롬인지 확인하기

s = input()
answer = 1
for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        answer = 0

print(answer)