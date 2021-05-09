def solution(N, stages):
    answer = []
    
    result = []
    total = len(stages)
    for i in range(1,N+1):
        if total == 0:
            miss = 0
        else:            
            cnt = stages.count(i)
            miss = cnt / total
            total -= cnt
        result.append([miss,i])

    result.sort(key = lambda x:(-x[0],x[1]))
    
    for i in result:
        answer.append(i[1])
    
    return answer
