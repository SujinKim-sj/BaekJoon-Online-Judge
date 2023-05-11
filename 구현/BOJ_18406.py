# 구현, 문자열
# 18406번. 럭키 스트레이트

n = input()

left = 0
for i in range(int(len(n) / 2)):
    left += int(n[i])

right = 0
for i in range(int(len(n) / 2), len(n)):
    right += int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")