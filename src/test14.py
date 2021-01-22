def solution(s):
    answer = int(1e9)
    length = len(s)
    
    if length == 1:
        return 1
    
    for i in range(1,length//2 +1):
        tmp = s[:i]
        cnt = 1
        result = ""
        for j in range(i,length,i):
            if s[j:j+i] == tmp:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ''
                result += str(cnt) + tmp
                cnt = 1
                tmp = s[j:j+i]
        if cnt ==1:
            cnt = ''
        result += str(cnt) + tmp
        answer = min(answer,len(result))
    
    return answer
