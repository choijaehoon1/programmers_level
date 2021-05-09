from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y,direc,board,n,m):
    INF = int(1e9)
    dist = [[INF]*m for _ in range(n)]
    dist[x][y] = 0
    q = deque()
    q.append([x,y,direc,0])
    
    while q:
        x,y,d,cost = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if k == d:
                new_cost = cost + 100
            else:
                new_cost = cost + 600
                
            if 0<=nx<n and 0<=ny<m:
                if dist[nx][ny] > new_cost and board[nx][ny] == 0:
                    dist[nx][ny] = new_cost
                    q.append([nx,ny,k,new_cost])
    # print(dist)
    return dist[n-1][m-1]

def solution(board):
    answer = int(1e9)
    n = len(board)
    m = len(board[0])
    for k in range(2):
        cost = bfs(0,0,k,board,n,m)
        answer = min(answer,cost)
    
    return answer
