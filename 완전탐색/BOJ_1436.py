# Brute Force
# 1436번. 영화감독 숌


N = int(input())    # N번째 영화

number = 666
count = 0

while(True):
    if "666" in str(number):
        count += 1
        if count == N:
            print(number)   # N번째 영화의 제목에 들어간 수
            break
    number += 1
