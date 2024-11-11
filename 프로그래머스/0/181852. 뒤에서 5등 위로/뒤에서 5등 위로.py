def solution(num_list):
    answer = []
    num_list.sort()
    answer = num_list[5:]
    answer.sort()
    return answer