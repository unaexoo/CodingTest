from collections import deque

def solution(maps):
    que = deque([(0, 0)])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue

            if maps[nx][ny] != 1:
                continue

            maps[nx][ny] = maps[x][y] + 1
            que.append((nx, ny))
    
    if maps[len(maps) - 1][len(maps[0]) - 1] > 1:
        answer = maps[len(maps) - 1][len(maps[0]) - 1]
    else :
        answer = -1
    return answer