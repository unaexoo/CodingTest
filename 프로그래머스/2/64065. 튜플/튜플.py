import re
from collections import Counter

def solution(s):
    answer = []
    s_list = re.findall(r'\d+', s)
    cnt = Counter(s_list)
    answer = list(map(int,sorted(cnt, key=lambda x:cnt[x],reverse=True)))
    return answer