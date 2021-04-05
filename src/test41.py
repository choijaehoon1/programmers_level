# 왼쪽, 오른쪽 괄호의 개수 맞는지 확인
def check(s):
    left_cnt = 0
    rigth_cnt = 0
    
    for i in s:
        if i == '(':
            left_cnt += 1
        if i == ')':
            rigth_cnt += 1                    
    if left_cnt == rigth_cnt:
        return True
    else:
        return False
    
# 적합한 괄호인지 확인(해당 함수에는 괄호의 개수가 같은 것만 들어옴 - (), (()), )(() 같은 형태)    
def proper(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        elif i == ')':
            if cnt == 0:
                return False # 올바르지 못한 경우
            cnt -= 1            
    return True

def solution(s):
    if check(s) == False:
        return False
    
    if proper(s) == False:
        return False
    
    return True
