from collections import deque
def solution(progresses, speeds):
    answer = []
    need_day = deque()
    
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            need_day.append((100-progresses[i])//speeds[i])
        else:
            need_day.append((100-progresses[i])//speeds[i] +1)
    
    while need_day:
        now = need_day.popleft()
        result = 1
        for i in range(len(need_day)):
            if now < need_day[i]:
                break
            result += 1
        answer.append(result)            
        
        while result > 1:
            need_day.popleft()
            result -= 1
        
    return answer
