# Greedy
# 1541번. 잃어버린 괄호

equtation = input().split('-')
answer = 0

for i in equtation[0].split('+'):
    answer += int(i)

for i in equtation[1:]:
    for j in i.split('+'):
        answer -= int(j)

print(answer)