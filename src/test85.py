def solution(gems):
    answer = [0,len(gems)-1]
    want_cnt = len(list(set(gems)))
    
    dic = {gems[0]:1}
    start = 0
    end = 0
    
    while start < len(gems) and end < len(gems):
        if len(dic) == want_cnt:
            if answer[1]-answer[0] > end-start:
                answer[0] = start
                answer[1] = end
            
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
            
        else:
            end += 1
            if end >= len(gems):
                break
            else:
                if dic.get(gems[end]) == None:
                    dic[gems[end]] = 1
                else:                 
                    dic[gems[end]] += 1
    
    answer[0] += 1
    answer[1] += 1
    
    return answer
