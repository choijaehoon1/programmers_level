from collections import deque

def check(s_list):
    tmp = []
    for i in s_list:
        if i in ['(','[','{']:
            tmp.append(i)
        else:
            if tmp == []:
                return False
            x = tmp.pop()
            if i == ')' and x != '(':
                return False
            if i == ']' and x != '[':
                return False
            if i == '}' and x != '{':
                return False
    if tmp != []:
        return False
    
    return True
            
    
def solution(s):
    answer = 0
    q = deque()
    for i in s:
        q.append(i)
    result = []            

    for i in range(len(q)):
        q.rotate(-1)
        tmp = ''
        for j in q:
            tmp += j
        result.append(tmp)
         
    for i in result:
        flag = check(list(i))
        if flag == True:
            answer+=1
    
    return answer
