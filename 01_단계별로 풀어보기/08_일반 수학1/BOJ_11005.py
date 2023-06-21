# 백준 단계별로 풀어보기 - 8. 일반 수학1
# 11005번. 진법 변환 2

n, b = map(int, input().split())

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ''

while n:
    answer += str(arr[n % b])
    n //= b

print(answer[::-1])  # 거꾸로 출력