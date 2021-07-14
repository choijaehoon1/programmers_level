import heapq

def solution(jobs):
    answer = 0
    
    cnt = 0 # 우선순위 큐에 들어가는 횟수 check
    time = 0 # 현재 시간
    start = -1 # 이전에 완료한 시간
    h = []
    while cnt < len(jobs):
        for job in jobs:
            inline,work = job
            if start < inline <= time:
                heapq.heappush(h,[work,inline])
        
        if h:
            w,i = heapq.heappop(h)
            start = time # 작업 완료시간을 현재시간으로 갱신
            cnt += 1
            time += w # 작업시간만큼 증가
            answer += (time - i) # 대기시간은 제외하고 구하기
        else: # 우선순위큐에 못들어가면 시간만 증가
            time += 1
        
    return answer//len(jobs)
