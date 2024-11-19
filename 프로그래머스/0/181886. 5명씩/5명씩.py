def solution(names):
    answer = []
    cnt = 0 
    for i in names :
        cnt+=1
        if cnt ==1 : 
            answer.append(i)
        elif cnt == 5:
            cnt =0
    return answer