# 삼성 SW 역량 테스트 기출 문제
# 백준 13458번. 시험 감독

# 1. 필요한 총감독관의 수 구하기

n = int(input())    # 시험장의 개수

# 각 시험장에 있는 응시자의 수
a = list(map(int, input().split()))

b, c = map(int, input().split())    # 총감독관과 부감독관이 감시할 수 있는 응시자의 수

count = 0

for i in range(len(a)):
    a[i] -= b
    count += 1                      # 총감독관 수 구하기
    if a[i] > 0:
        if int(a[i] % c) == 0:          # 부감독관 수 구하기
            if a[i] >= c:
                count += int(a[i] / c)
            else:
                count += 1
        else:
            count += (int(a[i] / c) + 1)

print(count)