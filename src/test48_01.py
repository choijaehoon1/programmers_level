# 시간 초과
from itertools import combinations
def solution(nums):
    answer = 0
    cnt = len(nums) // 2
    combi = list(combinations(nums,cnt))
    for i in combi:
        tmp = list(set(i))
        num  = len(tmp)
        answer = max(answer,num)
    return answer
