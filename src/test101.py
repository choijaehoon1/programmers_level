n,m = map(int,input().split())
board = [['*']*n for _ in range(m)]

for i in range(m):
    print(''.join(board[i]))
