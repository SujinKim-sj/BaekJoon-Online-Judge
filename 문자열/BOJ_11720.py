# String
# 11720번. 숫자의 합

n = int(input())
m = list(input())

sum = 0
for i in m:
    sum += int(i)

print(sum)