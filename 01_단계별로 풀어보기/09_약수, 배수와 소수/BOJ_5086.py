# 백준 단계별로 풀어보기 - 9. 약수, 배수와 소수
# 5086번. 배수와 약수

answer = ""

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    else:
        if m % n == 0:
            answer = "factor"
        elif n % m == 0:
            answer = "multiple"
        else:
            answer = "neither"
        print(answer)
