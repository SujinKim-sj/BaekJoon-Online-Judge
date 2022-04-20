# 재귀 10870번. 피보나치 수 5

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())

print(fib(n))
