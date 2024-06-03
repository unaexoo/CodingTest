def solution(k, score):
    answer = []
    tmp = []
    
    for i in score :
        tmp.append(i)
        tmp.sort(reverse=True)
        if len(tmp) > k :
            tmp.pop()
        answer.append(tmp[-1])
        
    return answer