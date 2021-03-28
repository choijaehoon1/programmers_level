from collections import deque
def solution(people, limit):
    answer = 0
    # Idea: 가장 무거운 사람을 먼저 태우는데 가장 작은 사람 한명 추가했을때 제한보다 작으면
    # 같이 태워 보내기(최대 2명까지 가능하므로하므로)
    people.sort()
    q = deque()
    for i in people:
        q.append(i)
    
    while q:
        if len(q) <= 1: # 1명일때는 그냥 추출
            q.pop()
            answer += 1
        
        if len(q) >= 2: # 2명이상일 때
            if q[0] + q[-1] <= limit: # 제일 무게 작은 사람 + 제일 큰 사람 비교
                q.popleft()
                q.pop()
                answer += 1
            else: # 제일 무게 큰 사람만 추출
                q.pop()
                answer += 1
    
    return answer
