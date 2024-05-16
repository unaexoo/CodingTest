import sys

N, M = map(int, input().split())

num_list = []

def backtraking():
    if len(num_list) == M:
        print(" ".join(map(str,num_list)))
        return
    
    for i in range(1, N+1):
        if i not in num_list :
            num_list.append(i)
            backtraking()
            num_list.pop()

backtraking()


