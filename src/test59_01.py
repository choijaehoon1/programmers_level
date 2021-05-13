# 3,5,7
import copy
def move(x1,y1,x2,y2,board):
    new_board = copy.deepcopy(board)
    cx,cy = x1,y1
    min_value = int(1e9)
    for k in range(4):
        while True:
            nx = dx[k] + x1
            ny = dy[k] + y1
            if cx == nx and cy == ny:
                new_board[cx][cy] = board[x1][y1]
                min_value = min(min_value,board[x1][y1])
                return new_board, min_value
            if cx<=nx<=x2 and cy<=ny<=y2:
                new_board[nx][ny] = board[x1][y1]
                min_value = min(min_value,board[x1][y1])
            else:
                break
            x1,y1 = nx,ny
                
            
dx = [0,1,0,-1]
dy = [1,0,-1,0]

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
        result = move(x1-1,y1-1,x2-1,y2-1,board)
        board = result[0]
        num = result[1]
        answer.append(num)
        
    return answer
