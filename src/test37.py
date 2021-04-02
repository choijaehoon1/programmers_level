def solution(arr):
    answer = [0,0]
    row = len(arr)
    
    def dfs(x,y,n):
        init = arr[x][y] # 초기값
        for i in range(x,x+n):
            for j in range(y,y+n):
                if init != arr[i][j]: # 다른 값이 발견되면
                    nn = n // 2 # 크기분할
                    dfs(x,y,nn) # 인덱스와 분할된 크기로 지정하여 dfs 수행 ex) 0,0,4
                    dfs(x+nn,y,nn) # 4,0,4
                    dfs(x,y+nn,nn) # 0,4,4
                    dfs(x+nn,y+nn,nn) # 4,4,4
                    return
        # 다 통과한 경우에는 해당하는 0이나 1의 값을 증가                
        answer[init] += 1                
    
    dfs(0,0,row) # 시작점 기준으로 인덱스 구해서 해결
    
    return answer
