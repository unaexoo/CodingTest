def solution(num_str):
    answer = 0
    num = int(num_str)
    while num :
        answer += num % 10
        num //=10
    return answer