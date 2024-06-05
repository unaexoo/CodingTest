def solution(cards1, cards2, goal):
    answer = 'No'

    if len(goal) > len(cards1) + len(cards2) :
        return answer
    
    i=0
    j=0
    tmp = []
    for g in goal :
        if i <len(cards1) and g == cards1[i] :
            tmp.append(cards1[i])
            i += 1
            
        if j <len(cards2) and g == cards2[j] :
            tmp.append(cards2[j])
            j += 1
        
    if tmp == goal :
        answer = 'Yes'
    else :
        answer = 'No' 
      
    return answer