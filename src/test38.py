def solution(board):
    answer = 0 # board의 값이 모두 0인 경우 check하기 위해 0으로 초기화
    
    # (1,1)부터 위,왼쪽, 왼쪽 대각선의 좌표를 확인하면서 board 갱신
    for i in range(1,len(board)): 
        for j in range(1,len(board[0])):
            if board[i][j] != 0: # dp 적용
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1
    # print(board)            
    # 가장 큰 값이 크기가 x인 정사각형으로 만들어질 수 있는 경우임
    for i in range(len(board)):
        answer = max(answer,max(board[i]))
    
    return answer**2
