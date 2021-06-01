# 인접행렬 시간초과 8,9 
from collections import deque

def bfs(node,n,board):
    dist = [-1]*(n+1)
    
    q = deque()
    q.append(node)
    dist[node] = 0
    
    while q:
        x = q.popleft()
        for i in range(1,n+1):
            if board[x][i] == 1 and dist[i] == -1:
                dist[i] = dist[x] + 1
                q.append(i)
    # print(dist)                
        
    return dist[1:],max(dist)
    
    
def solution(n, edge):
    answer = 0
    
    board = [[0]*(n+1) for _ in range(n+1)]
    for e in edge:
        a,b = e
        board[a][b] = 1
        board[b][a] = 1
    # print(board)
    dist,num = bfs(1,n,board)
    
    
    for i in dist:
        if i == num:
            answer += 1
    
    return answer
