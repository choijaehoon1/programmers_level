from collections import deque
def solution(priorities, location):
    q = deque()
    result = []
    for i in range(len(priorities)):
        q.append((priorities[i],i))
    
    while q:
        flag = False # 우선순위 체크용
        for i in q:
            if q[0][0] < i[0]:
                now = q.popleft()
                q.append(now)
                flag = True # 더 높은 우선순위가 있는 경우 체크
                break
        if flag == False: # for문에 해당하지 않으므로 가장 앞의 값이 우선순위가 가장 높은 것
            result.append(q.popleft())
    
    answer = 1
    for i in result:
        if i[1] == location:
            break
        answer += 1    
           
    return answer
