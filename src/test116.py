from collections import deque

def bfs(node,board,N,K):
    INF = int(1e9)
    dist = [INF for _ in range(N+1)]
    
    dist[node] = 0
    cost = 0
    q = deque()
    q.append([node,cost])
    
    while q:
        node,c = q.popleft()
        for i in board[node]:
            for j in range(1,N+1):
                if board[node][j] != 0:
                    cost = board[node][j] + c
                    if dist[j] > cost:
                        dist[j] = cost
                        q.append([j,cost])
    cnt = 0    
    for i in dist[1:]:
        if i <= K:
            cnt += 1
    return cnt

    
def solution(N, road, K):
    answer = 0
    board = [[0]*(N+1) for _ in range(N+1)]
    for r in road:
        a,b,c = r
        if board[a][b] == 0:
            board[a][b] = c
            board[b][a] = c
        else:
            board[a][b] = min(board[a][b],c)
            board[b][a] = min(board[b][a],c)
    
    answer = bfs(1,board,N,K)
        
    return answer
