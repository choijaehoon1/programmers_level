def solution(n):
    answer = []
    board = [[0]*n for _ in range(n)]
    length = n
    dx = [1,0,-1]
    dy = [0,1,-1]
    
    num = 0
    x,y = -1,0
    k = 0
    board[x][y] = num
    
    while n>=1:
        for i in range(n):
            num += 1
            nx = x + dx[k]
            ny = y + dy[k]
            board[nx][ny] = num
            x,y = nx,ny
        
        k = (k+1) %3
        n -= 1
    
    for i in range(length): # 주어지는 n을 조작하므로 변수 주의
        for j in range(length):
            if board[i][j] != 0:
                answer.append(board[i][j])
    
    return answer
