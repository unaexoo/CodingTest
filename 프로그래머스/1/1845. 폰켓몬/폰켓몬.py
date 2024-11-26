def solution(nums):
    answer = 0
    chose =len(nums)//2
    set_chose = len(set(nums))
    answer = min(chose,set_chose)
    return answer