
def solution(rows, columns, queries):
    answer = []
    tmp = 1
    board = [[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            board[i][j] = tmp
            tmp += 1
    
    for query in queries:
        x1,y1,x2,y2 = query
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        
        start = board[x1][y1]
        min_value = board[x1][y1]
        for i in range(x1,x2):
            board[i][y1] = board[i+1][y1]
            min_value = min(min_value,board[i][y1])
            
        for j in range(y1,y2):
            board[x2][j] = board[x2][j+1]
            min_value = min(min_value,board[x2][j])            
            
        for i in range(x2,x1,-1):
            board[i][y2] = board[i-1][y2]
            min_value = min(min_value,board[i][y2])                        
        
        for j in range(y2,y1,-1):
            board[x1][j] = board[x1][j-1]
            min_value = min(min_value,board[x1][j])                        
        
        board[x1][y1+1] = start
        answer.append(min_value)
        
    return answer
