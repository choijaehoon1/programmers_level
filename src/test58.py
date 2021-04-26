import sys
sys.setrecursionlimit(10**6)

answer = [0,0]
def dfs(arr,l,x,y,visit):
    global answer
    if l == 1:
        return
    
    check = arr[x][y]  
    tmp = 0
    for i in range(x,x+l):
        for j in range(y,y+l):
            if arr[i][j] == check and visit[i][j] == 0:
                tmp += 1
            else:
                break
            
    if tmp == l**2:
        answer[check] += 1
        for i in range(x,x+l):
            for j in range(y,y+l):
                visit[i][j] = 1   
        
    dfs(arr,l//2,x,y,visit)
    dfs(arr,l//2,x+l//2,y,visit)
    dfs(arr,l//2,x,y+l//2,visit)
    dfs(arr,l//2,x+l//2,y+l//2,visit)

    
def solution(arr):
    global answer
    global cnt
    length = len(arr)
    visit = [[0]*length for _ in range(length)]
    
    x,y = 0,0
    check = arr[x][y]  
    tmp = 0
    for i in range(x,x+length):
        for j in range(y,y+length):
            if arr[i][j] == check and visit[i][j] == 0:
                tmp += 1
            else:
                break
    
    if tmp == length**2:
        answer[check] += 1
        return answer
        
    if length == 1:
        for i in range(length):
            for j in range(length):
                answer[arr[i][j]] += 1
        return answer                
    
    dfs(arr,length//2,x,y,visit)
    dfs(arr,length//2,x+length//2,y,visit)
    dfs(arr,length//2,x,y+length//2,visit)
    dfs(arr,length//2,x+length//2,y+length//2,visit)
    
    for i in range(length):
        for j in range(length):
            if visit[i][j] == 0:
                answer[arr[i][j]] += 1
    
    return answer
