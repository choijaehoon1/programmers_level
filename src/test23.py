def divide(p):
    left_cnt = 0
    right_cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            left_cnt += 1
        if p[i] == ')':
            right_cnt += 1
        if left_cnt == right_cnt:
            return i

        
def check(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        if p[i] == ')':
            if cnt == 0:
                return False
            cnt -= 1    
    return True

def solution(p):
    answer = ''
#     if check(p) == True:
#         return p
    
    if len(p) == 0: return ''
    
    cnt = divide(p)
    u = p[:cnt+1]
    v = p[cnt+1:]
    # print(u,v)
    
    if check(u) == True:
        answer = u + solution(v)
    else:
        s = '('
        tmp = solution(v)
        s += tmp
        s += ')'
        u = list(u[1:-1])
        
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:    
                u[i] = '('
        answer = s + ''.join(u)
    
    return answer
