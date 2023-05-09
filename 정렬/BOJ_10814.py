# 안정정렬과 불안정정렬
# 10814번. 나이순 정렬

n = int(input())
member = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member.append([age, name])

# 나이 오름차순으로 정렬
member.sort(key=lambda x: x[0])

for i in member:
    print(i[0], i[1])