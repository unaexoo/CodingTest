N = int(input())
data_n = set(map(int, input().split()))

M = int(input())
data_m = list(map(int, input().split()))

for _ in data_m:
    if _ in data_n:
        print("1")
    else:
        print("0")