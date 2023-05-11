# 정수론
# 1929번. 소수 구하기

m, n = map(int, input().split())

for i in range(m, n + 1):
    if i == 1:      # 1은 소수가 아니므로 제외
        continue

    # 제곱근까지만 계산해도 소수 판별 가능
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:       # 약수가 존재하므로 소수가 아님
            break            # 더이상 검사할 필요가 없으므로 멈춤
    else:
        print(i)