def solution(n):
    answer = 0
    n_len = len(str(n))
    div = pow(10,n_len-1)
    sum = 0 
    while(n>0):
        answer += n//div
        n %= div
        print(answer)
        div/=10
    return answer