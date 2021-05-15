from itertools import combinations
def solution(relation):
    row = len(relation)
    column = len(relation[0])

    candidates = []
    for i in range(1,column+1):
        candidates.extend(combinations(range(column),i))
    # print(candidates)        
    
    final = []
    for keys in candidates:
        tmp = [tuple(item[k] for k in keys) for item in relation]
        # print(tmp)
        if len(set(tmp)) == row:
            final.append(keys)
    # print(final)            
    
    answer = set(final[:])
    # print(answer)
    
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i]) == len(set(final[i]) & set(final[j])):
                answer.discard(final[j])
    # print(answer)                
    answer = len(answer)
    
    return answer
