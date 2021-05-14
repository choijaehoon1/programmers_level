from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,n,m,maps):
    dist = [[-1]*m for _ in range(n)]
    dist[x][y] = 1
    q = deque()
    q.append([x,y])
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if dist[nx][ny] == -1 and maps[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])        
    return dist[n-1][m-1]                    
    

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    answer = bfs(0,0,n,m,maps)
    return answer
