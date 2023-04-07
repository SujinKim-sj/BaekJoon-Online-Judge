# Queue
# 2164번. 카드2

import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
for i in range(N):
    queue.append(i + 1)
    # queue.append(N - i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
    # queue.pop()
    # queue.appendleft(queue.pop())

print(queue.pop())
# print(queue.popleft())
