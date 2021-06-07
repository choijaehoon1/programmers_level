import heapq
def solution(jobs):
    answer = 0
    
    h = []
    cnt = 0
    start = -1
    time = 0
    while cnt < len(jobs):
        for job in jobs:
            a,b = job
            if start < a <=time:
                heapq.heappush(h,[b,a])
        
        if h:
            work,intime = heapq.heappop(h)
            answer += (time - intime  + work)
            start = time
            time += work        
            cnt += 1
        else:
            time += 1
    
    return answer//len(jobs)
