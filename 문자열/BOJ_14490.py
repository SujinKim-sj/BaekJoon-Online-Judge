# String
# 14490번. 백대열

# 유클리드 호제법을 통한 두 수의 최대공약수 구하기
def GCD(a, b):
    if b % a:
        return GCD(b % a, a)
    else:
        return a


n, m = map(int, input().split(':'))
a = GCD(n, m)

print(n // a, end='')
print(":", end='')
print(m // a, end='')