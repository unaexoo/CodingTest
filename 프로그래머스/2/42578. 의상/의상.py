from collections import Counter

def solution(clothes):
    answer = 1
    cnt = Counter([clo[1] for clo in clothes])
    for c in cnt.values() :
        answer *= (c+1)
    return answer-1