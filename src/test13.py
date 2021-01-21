def solution(n):
    answer = []
    board = [[0]*n for _ in range(n)]
    
    x,y = -1,0 # 초기값 설정, x는 행으로 처음에 1증가시켜서 0행으로 만들기 위해 -1로 설정
    num = 1
    for i in range(n):
        for j in range(i,n):
            # i를 가지고 나머지 연산 ex) 처음에 i가 0일 때는 4번 down연산임
            if i % 3 == 0: # 아래로 내려가는 경우 
                x+=1
            elif i % 3 == 1: # 오른쪽으로 한칸씩 이동
                y+=1
            elif i % 3 == 2: # 왼쪽 대각선으로 이동
                x-=1
                y-=1
            board[x][y] = num    
            num += 1
    
    for i in board:
        for j in i:
            if j != 0:
                answer.append(j)
    
    return answer
