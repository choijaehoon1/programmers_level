dx = [0,1,1] 
dy = [1,0,1]

def check(m,n,new_board,char,x,y):
    if char == '0': # 공백이면 False
        return False,x,y
    cnt = 1
    for k in range(3):
        nx = dx[k] + x
        ny = dy[k] + y
        if 0<=nx<m and 0<=ny<n:
            if new_board[nx][ny] == char:
                cnt += 1                
    if cnt == 4: # 4개가 붙어있는 경우만 True
        return True,x,y
    else:
        return False,x,y

def clear(cx,cy,new_board):
    # 4개 문자 '0'으로 공백처리
    new_board[cx][cy] = '0'
    for k in range(3):
        nx = dx[k] + cx
        ny = dy[k] + cy
        new_board[nx][ny] = '0'
    
    return new_board
    
def down(m,n,new_board,char,x,y):
    nx = dx[1] + x
    ny = dy[1] + y
    cx,cy = x,y # 내려가야할 값 초기 위치
    f_x,f_y = 0,0 # 최종 목적지
    
    if 0<=nx<m and 0<=ny<n and new_board[nx][ny] == '0' and new_board[x][y] != '0': # 자신은 공백이 아니고 다음칸이 공백인 경우만(1,1같은 경우는 걸러짐)
        x,y = nx,ny # 갱신
        while True: # 최종 도착지좌표 찾아 주기
            nx = x + dx[1]
            ny = y + dy[1]
            if 0<=nx<m and 0<=ny<n and new_board[nx][ny] != '0' and new_board[x][y] == '0': # 자신은 공백이고 다음 값이 공백이 아닌 경우 갱신
                f_x,f_y = x,y
                break
            if nx == m-1: # 마지막까지 몾찾으면 마지막 위치로 갱신
                f_x,f_y = m-1,y
                break
            x,y = nx, ny
    else:
        return new_board
        
    new_board[f_x][f_y] = char # 최종위치에 초기에 넘긴 (cx,cy)의 값 지정
    new_board[cx][cy] = '0' # 빈칸으로 변경
    for i in range(f_x-1,-1,-1): # 최종위치 한칸 위의 값부터 처음까지 확인
        tmp_x = cx - 1 # 초기 값 바로 위에 확인
        if tmp_x >= 0: # 처음행 보다 클때
            if new_board[tmp_x][f_y] != '0': # 값이 0이 아닌경우 내려주기
                new_board[i][f_y] = new_board[tmp_x][f_y]
                new_board[tmp_x][f_y] = '0'
        cx -= 1 # 다음 위칸 확인

    return new_board
            
    
def solution(m, n, board):
    answer = 0
    new_board = []
    for i in board:
        new_board.append(list(i))
    
    while True:    
        check_list = [] # 2*2 지워지는 좌표의 왼쪽 위의 값 저장
        for i in range(m):
            for j in range(n):
                flag,i,j = check(m,n,new_board,new_board[i][j],i,j)
                if flag:
                    check_list.append([i,j])
        
        if check_list == []: # 체크할것이 없으면 종료
            for i in range(m):
                answer += new_board[i].count('0')
            return answer
        
        # 해당되는 것 지우기
        for cx,cy in check_list:
            new_board = clear(cx,cy,new_board)
        
        tmp_list = [] # 해당하는 왼쪽위 좌표에서 내려오게 될 좌표의 바로 위 값들 저장
        # ex) 테스트 2번 (0,0), (0,1), (1,2), (0,4), (0,5), (1,1) -> 1,1은 down함수에 의해 조건처리되므로 신경 x
        for cx,cy in check_list:
            if cx-1 >= 0: # 처음 행 이상일 때만
                tmp_list.append([cx-1,cy])
                tmp_list.append([cx-1,cy+1])
        
        for tx,ty in tmp_list:
            new_board = down(m,n,new_board,new_board[tx][ty],tx,ty) # 내리기
        
