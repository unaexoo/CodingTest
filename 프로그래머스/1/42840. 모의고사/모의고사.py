def solution(answers):
    answer = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    sum_list = [0]*3
    for i in range(len(answers)):
        if answers[i] == num1[i%5]:
             sum_list[0] += 1
        if answers[i] == num2[i%8]:
            sum_list[1] +=1
        if answers[i] == num3[i%10]:
            sum_list[2] += 1
            
    res = max(sum_list) 

    for i in range(len(sum_list)):
        if sum_list[i] == res:
            answer.append(i+1)
    return answer