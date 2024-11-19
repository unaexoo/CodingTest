def solution(my_string, alp):
    answer = my_string.replace(alp,chr(ord(alp)-32))
    return answer