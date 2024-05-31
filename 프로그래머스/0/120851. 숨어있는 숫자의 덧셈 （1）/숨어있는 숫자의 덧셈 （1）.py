def solution(my_string):
    answer = 0
    num = [1,2,3,4,5,6,7,8,9]
    for i in my_string :
        if not("a"<= i<="z" and "A"<= i<="Z") :
            try : 
                n= int(i)
            except ValueError :
                continue
            
            if n in num :
                answer += n
    return answer