# 백준 단계별로 풀어보기 - 5. 문자열
# 9086번. 문자열

test = int(input())

for i in range(test):
    s = input()
    print(s[0] + s[-1])