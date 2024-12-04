def solution(num, total):
    answer = []
    sum = (total*2//num-num+1)//2
    for i in range(0,num):
        answer.append(sum+i)
    return answer
