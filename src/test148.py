answer = 0

def dfs(begin, target, words, visit):
    global answer
    
    stack = []
    stack.append(begin)
    
    while stack:
        node = stack.pop()
        if node == target:
            return answer
        
        for i in range(len(words)):
            cnt = 0
            for j in range(len(begin)):
                if words[i][j] != node[j]:
                    cnt += 1

            if cnt == 1 and visit[i] == 0:
                visit[i] = 1
                stack.append(words[i])
        answer += 1                
        

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visit = [0] * len(words)
    dfs(begin, target, words, visit)    
    
    return answer
