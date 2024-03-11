import sys

N = int(input())
divisor = list(map(int, sys.stdin.readline().split()))

divisor.sort()
res = divisor[0] * divisor[len(divisor)-1]
print(res)