from collections import Counter
def solution(want, number, discount):
    answer = 0
    dict_list = dict(zip(want,number))
    cout = {}
    for i in range(len(discount)-9) :
        count = Counter(discount[i:i+10])
        if count == dict_list:
            answer+=1
    
    return answer