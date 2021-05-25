def solution(s):
    answer = ''
    data = list(map(int,s.split()))
    answer += str(min(data)) + ' '
    answer += str(max(data))
    
    return answer
