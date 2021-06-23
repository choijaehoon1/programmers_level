def solution(n, results):
    answer = 0
    INF = int(1e9)
    board = [[INF]*(n+1) for _ in range(n+1)]
    
    
    for result in results:
        a,b = result
        board[a][b] = 1 # 항상 이기는 경우 check
        
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                board[i][j] = 0
    
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                board[a][b] = min(board[a][b],board[a][k] + board[k][b])
    
    check = [True] * (n+1)
    
    # 한 사람씩 확인해가며 게임을 해봤는지 확인
    for i in range(1,n+1): 
        for j in range(1,n+1):
            if i == j:
                continue
            # 경로가 존재하지 않으면 게임을 하지 않은 것(양쪽 모두 INF이면 경기 안해서 결과 모르는 경우)
            if board[i][j] == INF and board[j][i] == INF:
                check[i] = False
                break
    
    for i in range(1,n+1):
        if check[i]:
            answer += 1
        
    return answer

