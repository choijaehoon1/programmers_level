def trans(num):
    answer = ''
    while num > 0:
        answer = str(num%2) + answer
        num //= 2
    return answer        
        

def solution(s):
    zero_cnt = 0
    time = 0

    if s == "1":
        return [0,0]
    else:
        while s != "1":
            new_s = s.replace('0','')
            length = len(new_s)
            zero_cnt += (len(s) - length)
            time += 1
            result = trans(length)
            # print(result)
            s = result
    return [time, zero_cnt]
    
