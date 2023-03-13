# Stack
# 2812번 크게 만들기

n, k = map(int, input().split())
number = list(input())

answer = []
cnt = k
for num in number:
    while answer and cnt > 0 and answer[-1] < num:
        del answer[-1]
        cnt -= 1
    answer.append(num)

# .join(리스트) : 리스트 속 문자들을 합쳐 문자열로 반환
print(''.join(answer[:n - k]))

