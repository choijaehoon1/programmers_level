def solution(d, budget):
    answer = 0
    d.sort()
    
    while True:
        for i in d:
            if i <= budget:
                answer += 1
                budget -=i
            else:
                break
        break                
    
    return answer
