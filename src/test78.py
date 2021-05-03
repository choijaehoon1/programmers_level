from itertools import combinations
import math
def sosu(num):
    if num <= 1:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True        

def solution(nums):
    answer = 0
    combi_list = []
    combi_list.append(list(combinations(nums,3)))    
    
    # t_set = set() # 문제 잘 읽기(서로 다른 3개 골라서 같은 값이 나와도 되는 경우이므로 set 불필요)
    check_list = []
    for combi in combi_list:  
        for c in combi:
            check_list.append(sum(c))
            # t_set.add(sum(c))
    
    # check_list = list(t_set)
    for i in check_list:
        if sosu(i):
            answer += 1

    return answer
