# 재귀
# 11729번. 하노이탑 이동 순서

def hanoi(num, start, to, end):
    if num == 1:
        print("1일때", start, end)
    else:
        hanoi(num - 1, start, end, to)
        print("나머지", start, end)
        hanoi(num - 1, to, start, end)


num = int(input())
print(2 ** num - 1)
hanoi(num, 1, 2, 3)
