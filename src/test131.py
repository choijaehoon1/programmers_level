def solution(s):
    answer = ''
    data = s.split(' ')
    
    for i in data:
        if i == '':
            answer += ' '
        else:
            tmp = list(i.lower())

            tmp[0] = tmp[0].upper()
            
            for k in tmp:
                answer += k
            answer += ' '            
                
    answer = answer[:-1]
    return answer
