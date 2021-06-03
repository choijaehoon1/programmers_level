from collections import deque

def bfs(node,visit,n,computers):
    visit[node] = 1
    q = deque()
    q.append(node)
    
    while q:
        x = q.popleft()
        for i in range(n):
            if computers[x][i] == 1 and visit[i] == 0:
                visit[i] = 1
                q.append(i)
    

def solution(n, computers):
    answer = 0
    visit = [0]*n
    
    for i in range(n):
        if visit[i] == 0:
            answer += 1
            bfs(i,visit,n,computers)
    
    return answer
