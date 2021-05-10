def solution(dartResult):
    answer = 0
    
    dart_list = list(dartResult)
    tmp = ''
    
    flag = False
    result = []
    idx = 0
    for i in range(len(dart_list)-1):
        tmp += dart_list[i]
        if tmp == '1' and dart_list[i+1] == '0':
            flag = True
            i += 1
        
        if flag:
            flag = False
            continue
        
        if dart_list[i+1].isnumeric():
            result.append(tmp)
            tmp = ''
            flag = False
        if len(result) == 2:
            idx = i
            break
    last = ''.join(dart_list[idx+1:])
    result.append(last)
    
    
    score = ['S','D','T']
    ago = 0
    for r in result:
        tmp = ''
        num = 0
        for i in r:
            if i in score:
                if i == 'S':
                    num = int(tmp)**1
                elif i == 'D':
                    num = int(tmp)**2
                elif i == 'T':
                    num = int(tmp)**3                    
            elif i.isnumeric():            
                tmp += i
            else:
                if i == '*':
                    answer -= ago                    
                    ago *= 2
                    num *= 2
                    answer += ago                    
                elif i == '#':                    
                    num = -num
        print(num,ago,answer)                    
        answer += num
        ago = num
                    
    return answer
