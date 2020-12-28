from itertools import combinations
def solution(numbers):
    answer = []
    
    for cx,cy in combinations(numbers,2):
        tmp = cx + cy
        if tmp not in answer:
            answer.append(tmp)
    answer.sort()            
    
    
    return answer
