def solution(n):
    answer = [[0]*n for _ in range(n)]
    num = 0
    y = 0
    x = -1
    size = n
    step = 1
    
    while size > 0 :
        for _ in range(size) :
            x+= step
            num += 1
            answer[y][x] = num
        size -= 1
        
        for _ in range(size):
            y+= step
            num += 1
            answer[y][x] = num
        step *= -1
    return answer