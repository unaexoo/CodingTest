
lens = int(input())

res = list(input())
for i in range(lens-1) :
    file = input()
    for j in range(len(res)):
        if res[j] != file[j] :
            res[j] = "?"

print(''.join(res))