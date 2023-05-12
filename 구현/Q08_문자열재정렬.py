# 이것이 취업을 위한 코딩테스트다
# 구현 - Q08. 문자열 재정렬

s = input()
alpha = []
num = 0

for i in range(len(s)):
    if s[i].isalpha():
        alpha.append(s[i])
    else:
        num += int(s[i])

print(''.join(sorted(alpha)) + str(num))
