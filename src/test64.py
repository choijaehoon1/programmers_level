def solution(s):
    answer = 0
    flag = False
    
    if s[0]:
        if s == '-':
            flag = True
    if flag == True:
        answer = -int(s[1:])
    else:
        answer = int(s)
    
    return answer
