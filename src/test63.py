
def possible(x,n):
    tmp = 0
    for i in range(x,n+1):
        tmp += i
        if tmp == n:
            return True
        if tmp > n:
            break
    return False            
    

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if possible(i,n):
            answer += 1
    
    return answer
