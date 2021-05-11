import sys
sys.setrecursionlimit(10**6)
answer = 0
def dfs(numbers,target,idx):
    global answer
    
    if idx == len(numbers):
        if sum(numbers) == target:
            answer += 1
        return
    
    else:
        dfs(numbers,target,idx+1)
        numbers[idx] *= -1
        dfs(numbers,target,idx+1)
        
        
def solution(numbers, target):
    global answer
    visit = [0 for _ in range(len(numbers))]
    dfs(numbers,target,0)
    
    return answer
