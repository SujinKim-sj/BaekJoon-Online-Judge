# 백준 단계별로 풀어보기 - 8. 일반 수학1
# 2720번. 세탁소 사장 동혁

t = int(input())

for i in range(t):
    c = int(input())
    q = c // 25                 # 쿼터
    d = c % 25 // 10            # 다임
    n = c % 25 % 10 // 5        # 니켈
    p = c % 25 % 10 % 5 // 1    # 페니
    print(q, d, n, p)
