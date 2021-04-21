def solution(dirs):
    dir_list = list(dirs)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    check_list = []
    answer = 0
    x,y = 0,0
    for d in dir_list:    
        if d == 'U':
            nx = dx[3] + x
            ny = dy[3] + y
            if -5 <= nx <= 5 and -5 <= ny <= 5:
                if [x,y,nx,ny] not in check_list and [nx,ny,x,y] not in check_list:
                    answer += 1
                    check_list.append([x,y,nx,ny])   
            else:
                continue
            x,y = nx,ny
            
        if d == 'D':
            nx = dx[2] + x
            ny = dy[2] + y
            if -5 <= nx <= 5 and -5 <= ny <= 5:
                if [x,y,nx,ny] not in check_list and [nx,ny,x,y] not in check_list:
                    answer += 1
                    check_list.append([x,y,nx,ny])                       
            else:
                continue                    
            x,y = nx,ny
        
        if d == 'L':
            nx = dx[0] + x
            ny = dy[0] + y
            if -5 <= nx <= 5 and -5 <= ny <= 5:
                if [x,y,nx,ny] not in check_list and [nx,ny,x,y] not in check_list:
                    answer += 1
                    check_list.append([x,y,nx,ny])   
            else:
                continue                    
            x,y = nx,ny
            
                    
        if d == 'R':
            nx = dx[1] + x
            ny = dy[1] + y
            if -5 <= nx <= 5 and -5 <= ny <= 5:
                if [x,y,nx,ny] not in check_list and [nx,ny,x,y] not in check_list:
                    answer += 1
                    check_list.append([x,y,nx,ny])                       
            else:
                continue                    
            x,y = nx,ny
    
    return answer
