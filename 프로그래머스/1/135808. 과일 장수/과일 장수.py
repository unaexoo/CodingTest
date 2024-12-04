def solution(k, m, score):
    answer = 0
    idx = m-1
    score = sorted(score,reverse=True)
    for i in range(0,len(score)//m):
        answer += score[idx]*m
        idx +=m
    return answer