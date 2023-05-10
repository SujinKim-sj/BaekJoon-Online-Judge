# String
# 9935번. 문자열 폭발

# 스택, 슬라이딩 윈도우 알고리즘 사용

s = str(input())
bomb = str(input())
left = []

start = 0
end = len(s) - 1

while start <= end:
    tof = True
    left.append(s[start])
    start += 1
    # print("left", left)

    if len(left) >= len(bomb):
        for i in range(len(bomb)):
            # 끝에서 두자리 문자열을 폭탄 문자열과 비교
            if left[len(left) - len(bomb) + i] != bomb[i]:
                tof = False
                break
        if tof:
            for i in range(len(bomb)):
                left.pop()

# 스택의 길이가 0이면
if len(left) == 0:
    print("FRULA")
else:
    for i in range(len(left)):
        print(left[i], end='')
