answer = 0
def dfs(numbers,target,i):
    global answer
    if i == len(numbers): # 끝까지 수행했을 때만 확인(i가 인덱스 범위 벗어날때가 끝까지 수행한 것임)
        if sum(numbers) == target: # 종료 조건
            answer += 1
            return
    else:
        dfs(numbers,target,i+1) # 재귀먼저 수행(맨 처음 주어진 numbers가 target과 같을수도 있으므로)
        numbers[i] *= -1 # 값을 바꿔주고 (원복도 수행 됨)
        dfs(numbers,target,i+1) # 바뀐 numbers로 재귀 수행

def solution(numbers, target):
    global answer
    dfs(numbers,target,0)    
    return answer
