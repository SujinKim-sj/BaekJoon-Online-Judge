# 백준 단계별로 풀어보기 - 9. 약수, 배수와 소수
# 9506번. 약수들의 합

while True:
    n = int(input())
    arr = []
    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            arr.append(i)

    if sum(arr) == n:
        print(n, "= ", end="")
        for i in range(len(arr)):
            if i == len(arr) - 1:
                print(arr[i], end="")
            else:
                print(arr[i], "+", end=" ")
        print("")
    else:
        print(n, "is NOT perfect.")