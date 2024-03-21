from collections import deque
import sys

N = int(sys.stdin.readline())

deq = deque()
for i in range(1, N + 1):
    deq.append(i)

i = 0
while len(deq) > 1:
    deq.popleft()
    tmp = deq.popleft()
    deq.append(tmp)

print(deq.pop())