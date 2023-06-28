# 백준 단계별로 풀어보기 - 8. 일반 수학1
# 1193번. 분수찾기

n = int(input())

line = 0    # 사선 라인
max_n = 0   # n의 라인에서 가장 큰 숫자

# 입력받은 정수가 위치한 사선 라인이 몇 번째인지, 사선 라인에서 제일 큰 수 알아내기
while n > max_n:
    line += 1
    max_n += line

gap = max_n - n
if line % 2 == 0:   # 사선 라인이 짝수번 째일 때
    boonja = line - gap # 분자
    boonmo = gap + 1    # 분모
else:               # 사선 라인이 홀수번 째일 때
    boonja = gap + 1
    boonmo = line - gap

print(str(boonja) + "/" + str(boonmo))