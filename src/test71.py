def solution(n):
    answer = 0
    array = []
    str_n = str(n)
    for i in str_n:
        array.append(int(i))
    array.sort(reverse=True)        
    tmp = ''
    for i in array:
        tmp += str(i)
    answer = int(tmp)        
    
    return answer
