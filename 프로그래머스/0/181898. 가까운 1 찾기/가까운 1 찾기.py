def solution(arr, idx):
    answer = -1
    for i in range(len(arr)):
        if idx <= i and arr[i]==1 :
            return i
    return answer