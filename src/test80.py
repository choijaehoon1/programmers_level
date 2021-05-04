from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def find(i,board):
    for x in range(4):
        for y in range(3):
            if board[x][y] == i:
                return x,y
    
def bfs(x,y,c_x,c_y):
    dist = [[-1]*3 for _ in range(4)]
    dist[x][y] = 0
    q = deque()
    q.append([x,y])
    
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<4 and 0<=ny<3:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx,ny])
    return dist[c_x][c_y]                        
    

def solution(numbers, hand):
    answer = ''
    board = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['*',0,'#']
    ]
        
    l_x,l_y = 3,0
    r_x,r_y = 3,2
    
    for i in numbers:
        if i in [1,4,7]:
            if i == 1:
                l_x,l_y = 0,0
            elif i == 4:
                l_x,l_y = 1,0                
            elif i == 7:
                l_x,l_y = 2,0                    
            answer += 'L'                
        elif i in [3,6,9]:
            if i == 3:
                r_x,r_y = 0,2
            elif i == 6:
                r_x,r_y = 1,2                
            elif i == 9:
                r_x,r_y = 2,2                    
            answer += 'R'
        else:
            c_x,c_y = find(i,board)                    
            l_num = bfs(l_x,l_y,c_x,c_y)
            r_num = bfs(r_x,r_y,c_x,c_y)
            if l_num == r_num:
                if hand == 'right':
                    answer += 'R'
                    r_x,r_y = c_x,c_y
                else:            
                    answer += 'L'
                    l_x,l_y = c_x,c_y
            elif l_num < r_num:
                answer += 'L'
                l_x,l_y = c_x,c_y
            elif l_num > r_num:
                answer += 'R'
                r_x,r_y = c_x,c_y 
        
    return answer
