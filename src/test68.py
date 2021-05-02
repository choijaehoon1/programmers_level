def solution(s):
    answer = ''
    tmp = s.split(' ')
    
    for t in tmp:
        new_t = ''
        for i in range(len(t)):
            if i % 2 == 0:
                new_t += t[i].upper()
            else:
                new_t += t[i].lower()
        answer += new_t + ' '
    answer = answer[:-1]        
    
    return answer
