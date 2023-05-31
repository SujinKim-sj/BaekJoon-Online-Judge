# 단계별로 풀어보기 - 2.조건문
# 백준 2480번. 주사위 세개

arr = list(map(int, input().split()))

answer = 0
if arr.count(arr[0]) == 3 or arr.count(arr[1]) == 3 or arr.count(arr[2]) == 3:
    answer = 10000 + (arr[0] * 1000)
elif arr.count(arr[0]) == 2:
    answer = 1000 + arr[0] * 100
elif arr.count(arr[1]) == 2:
    answer = 1000 + arr[1] * 100
elif arr.count(arr[2]) == 2:
    answer = 1000 + arr[2] * 100
else:
    answer = max(arr) * 100

print(answer)


# 다른 사람의 풀이
a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)