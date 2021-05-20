# 효율성 실패
from collections import deque

def bfs(node,visit,dist,n):
    q = deque()
    visit[node] = 1
    dist[node] = 0
    q.append(node)
    
    while q:
        x = q.popleft()
        if x == n:
            return dist[n]
        
        if x < n+1:
            if x*2 < n+1:
                if dist[x*2] == -1 and visit[x*2] == 0:
                    dist[x*2] = dist[x]
                    visit[x*2] = 1
                    q.appendleft(x*2)
            if x+1 < n+1:                     
                if dist[x+1] == -1 and visit[x+1] == 0:
                    dist[x+1] = dist[x] + 1
                    visit[x+1] = 1
                    q.append(x+1)
    

def solution(n):
    ans = 0
    
    visit = [0 for _ in range(n+1)]
    dist = [-1 for _ in range(n+1)]
    ans = bfs(0,visit,dist,n)
    

    return ans
