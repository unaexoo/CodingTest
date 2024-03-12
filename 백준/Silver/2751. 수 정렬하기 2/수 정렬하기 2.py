N = int(input())
x = []
for i in range(N):
    x.append(int(input()))

x.sort(reverse=True) 
for i in range(N):
    print(x.pop())