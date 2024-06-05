def solution(num_list):
    answer = 0
    sum = 0
    dots = 1
    for i in num_list :
        dots *= i
        sum += i
    sum_square = sum*sum
    
    print(dots)
    print(sum_square)
    if dots < sum_square :
        answer = 1
    else :
        answer = 0 

    return answer