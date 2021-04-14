# 그리디
def solution(nums):
    check_list = list(set(nums))
    cnt = len(nums)//2
    if cnt <= len(check_list):
        return cnt
    else:
        return len(check_list)
    
