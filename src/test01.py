from collections import deque
def solution(board, moves):
    answer = 0
    q = deque()
    
    for i in moves:
        for j in range(len(board)):
            # 큐가 비었고 board의 값이 0이 아닌 경우나 board의 값이 0이 아니고 큐의 마지막원소와 같은 경우
            if (len(q) == 0 and board[j][i-1] != 0) or (board[j][i-1] != 0 and board[j][i-1] != q[-1]):
                q.append(board[j][i-1])
                board[j][i-1] = 0
                break
            
            # 보드값이 0이 아니고 큐의 마지막 원소값과 같은 경우
            if board[j][i-1] != 0 and board[j][i-1] == q[-1]:
                q.append(board[j][i-1])
                board[j][i-1] = 0
                q.pop()
                q.pop()
                answer += 2
                break
    
    return answer
