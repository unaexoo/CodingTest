def solution(num_list, n):
    answer = []
    for i in range(len(num_list)) :
        if i==n or i>n:
            answer.append(num_list[i])
            
    for i in range(n):
        answer.append(num_list[i])
    return answer