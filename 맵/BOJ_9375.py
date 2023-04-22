# Map

# 9375번. 패션왕 신해빈

testcase = int(input())

for i in range(testcase):
    map = {}
    answer = 1
    n = int(input())    # 의상의 수

    for j in range(n):
        a, b = input().split()  # 의상의 이름, 종류
        if not b in map:
            map[b] = 1
        else:
            map[b] += 1

    for k in map.keys():
        answer = answer * (map[k] + 1)

    # 옷을 전부 입지 않은 값을 포함하므로 -1
    print(answer - 1)
