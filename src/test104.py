def solution(s):
    length = len(s)
    answer = length
    
    for i in range(1,length//2+1):
        tmp = ''
        result = ''
        start = s[:i]
        cnt = 1
        
        for k in range(i,length,i):
            if start == s[k:k+i]:        
                cnt += 1
                tmp = str(cnt) + start
            else:
                if cnt > 1:
                    tmp = str(cnt) + start
                    result += str(cnt) + start
                else:                    
                    tmp = start
                    result += start
                
                start = s[k:k+i]
                cnt = 1
                tmp = ''
                
        if tmp == '':
            check = result + start                    
        else:                
            check = result + tmp
        answer = min(answer,len(check))
        
    return answer
