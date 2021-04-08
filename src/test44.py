def binary(n):
    tmp_str = ''
    while n > 0:
        tmp_str = str((n % 2)) + tmp_str
        n //= 2
    return tmp_str        

def ten(str_num):    
    result = 0
    for i in range(len(str_num)-1,-1,-1):
        if str_num[i] == '1':
            result += 2**(len(str_num)-1 - i)
    return result            
    
def solution(n):
    answer = 0
    num = binary(n)
    cnt = num.count('1')
    
    while True:    
        n += 1
        tmp_num = binary(n)
        tmp_cnt = tmp_num.count('1')
        if cnt == tmp_cnt:
            print(tmp_num)
            answer = ten(tmp_num)
            break
    
    return answer
