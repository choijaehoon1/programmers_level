# 문자열 나누는 인덱스 반환 함수
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

# p에는 균형잡힌 문자열 형태로만 들어오게 됨 ex) (()), ())(        
def check(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        # 제일 먼저 들어오는게 )인 경우 False이고 ())(와 같은 경우 False 리턴됨    
        if p[i] == ')':
            if cnt == 0: 
                return False
            cnt -= 1    
    return True

def solution(p):
    # p가 이미 올바른 괄호 문자열인 경우
    if check(p) == True:
        return p
    
    # 빈문자열인 경우
    if len(p) == 0: return ''
    
    # u와 v는 균형잡히게 반환 됨
    cnt = divide(p)
    u = p[:cnt+1]
    v = p[cnt+1:]
    # print(u,v)
    
    # 올바른 괄호 문자열인 경우
    if check(u) == True:
        return u + solution(v)
    else: # 올바른 괄호 문자열이 아닌 경우
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
        return s + ''.join(u)
        
