# 백준 단계별로 풀어보기 - 6. 심화 1
# 25206번. 너의 평점은

sumCredit = 0 # 학점의 총합
sumGrade = 0  # 전공과목별(학점 X 과목평점) 합

for _ in range(20):
    name, credit, grade = map(str, input().split()) # 과목명, 학점, 등급 입력받기

    if grade == 'A+':
        grade2 = 4.5
    elif grade == 'A0':
        grade2 = 4.0
    elif grade == 'B+':
        grade2 = 3.5
    elif grade == 'B0':
        grade2 = 3.0
    elif grade == 'C+':
        grade2 = 2.5
    elif grade == 'C0':
        grade2 = 2.0
    elif grade == 'D+':
        grade2 = 1.5
    elif grade == 'D0':
        grade2 = 1.0
    elif grade == 'F':
        grade2 = 0.0
    else:
        continue

    sumCredit += float(credit)
    sumGrade += float(credit) * grade2

answer = round(sumGrade / sumCredit, 6)
print(sumGrade / sumCredit)
