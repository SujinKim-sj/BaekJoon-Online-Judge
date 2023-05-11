# 정수론
# 5347번. LCM

# 유클리드 호제법 이용
def LCM(a, b):  # 최소공배수
    return (a * b) // GCD(a, b)


def GCD(a, b):  # 최대공약수
    if b % a:
        # a를 b로 나눈 나머지 R을 구한다
        return GCD(b % a, a)
    else:
        # 나누어 떨어지면 반환
        return a


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))