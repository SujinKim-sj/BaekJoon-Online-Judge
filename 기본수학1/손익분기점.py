# 기본 수학 - 1단계. 손익분기점

def bep(a, b, c):
    if b >= c:
        return -1
    else:
        return int(a // (c - b) + 1)


a, b, c = map(int, input().split())
print(bep(a, b, c))
