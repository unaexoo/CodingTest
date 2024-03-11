result = []
num = 10000
def selfnum(n):
    for i in range(1, n+1) :
        res = i
        tmp = i
        while tmp > 0:
            res += tmp%10
            tmp //= 10
        result.append(res)

selfnum(num)           
for i in range(1,num+1):
    if i not in result:
        print(i)