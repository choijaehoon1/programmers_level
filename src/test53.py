def solution(n, words):
    answer = []
    check = []
    start = words[0][-1]
    cnt = 1
    cycle = 1
    check.append(words[0])
    
    for i in range(1,len(words)):
        cnt += 1
        if words[i] in check:
            return [cnt,cycle]
        
        if start == words[i][0]:
            start = words[i][-1]
            check.append(words[i])
        else:
            return [cnt,cycle]
        
        if cnt >= n:
            cycle += 1
            cnt = 0
                  
    if len(check) == len(words):
        return [0,0]
    
    return answer
