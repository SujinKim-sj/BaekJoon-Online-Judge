# Back Traking
# 14888번. 연산자 끼워넣기

def backTraking(index, sum):
    global minAns
    global maxAns
    # 백트래킹의 핵심
    if index == N - 1:
        if minAns > sum : minAns = sum
        if maxAns < sum : maxAns = sum
        return

    for i in range(4):  # 연산자 개수만큼
        temp = sum
        if operator[i] == 0: continue
        if i == 0: sum += numArr[index + 1]
        elif i == 1: sum -= numArr[index + 1]
        elif i == 2: sum *= numArr[index + 1]
        else:
            if sum < 0: sum = abs(sum) // numArr[index + 1] * -1
            else: sum //= numArr[index + 1]

        operator[i] -= 1        # operator[i] = 0이면 연산자를 모두 사용한 것임
        backTraking(index + 1, sum)
        operator[i] += 1
        sum = temp

N = int(input())
numArr = list(map(int, input().split()))
operator = list(map(int, input().split()))

# 무한으로 설정
minAns = float('Inf')
maxAns = float('-Inf')

backTraking(0, numArr[0])
print(maxAns)
print(minAns)
