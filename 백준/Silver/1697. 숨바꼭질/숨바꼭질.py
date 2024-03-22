import sys
from collections import deque

n, k = map(int, input().split())

def bfs() :
    visited = [False] * 100001
    queue = deque([(n,0)]) # 좌표, 이동횟수
    visited[n] = True # 방문을 했다면
    while queue:
        x, cnt = queue.popleft()
        
        if x == k :
            return cnt
        
        for i in (x-1, x+1, 2*x) : 
            if 0<=i < 100001 and not visited[i] :
                queue.append((i,cnt+1))
                visited[i] = True
            
print(bfs())