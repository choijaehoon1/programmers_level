def solution(s, n):
    answer = ''
    upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in s:
        if i in upper:
            tmp = ord(i) - ord('A')
            if tmp + n >= 26:
                num = tmp + n - 26
                answer += upper[num]
            else:
                answer += upper[tmp+n]
        if i in lower:                
            tmp = ord(i) - ord('a')
            if tmp + n >= 26:
                num = tmp + n - 26
                answer += lower[num]
            else:
                answer += lower[tmp+n]
        if i == ' ':                
            answer += ' '
    
    return answer
