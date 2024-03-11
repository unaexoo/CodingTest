import sys

N = int(input())
one_card = list(map(int, sys.stdin.readline().split()))
M = int(input())
two_card = list(map(int, sys.stdin.readline().split()))

dic = {i: 0 for i in two_card}

for i in one_card:
    if i in dic:
        dic[i] += 1

for i in two_card:
    print(dic[i], end=' ')
