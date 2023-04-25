# Priority Queue
# 1715번. 카드 정렬하기

import heapq

N = int(input())

card = list(int(input()) for _ in range(N))

# N개의 카드를 힙으로 변환
heapq.heapify(card)
answer = 0

# 카드의 개수가 1이 아닐 때까지 반복(N이 1이면 answer은 0)
while len(card) != 1:
    # 우선순위 큐에서 가장 작은 값 2개 꺼내기
    first = heapq.heappop(card)
    second = heapq.heappop(card)

    sum = first + second
    answer += sum

    # 합친 값을 다시 우선순위 큐에 삽입
    heapq.heappush(card, sum)

print(answer)