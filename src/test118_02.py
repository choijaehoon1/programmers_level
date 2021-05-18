def binary(n):
    tmp = ''
    while n > 0:
        t = n % 2 
        tmp = str(t) + tmp
        n //= 2
    return tmp


def solution(numbers):
    answer = []
    for number in numbers:
        bi = binary(number)
        bi = '0' + bi
        new_bi = bi
        bi = list(bi)
        new_bi = list(new_bi)
        
        idx = 0
        for i in range(len(bi)-1,-1,-1):
            if bi[i] == '0':
                new_bi[i] = '1'
                idx = i
                break
        
        if idx + 1 < len(new_bi):
            new_bi[idx+1] = '0'
        
        tmp = 0 
        for i in range(len(new_bi)-1,-1,-1):
            tmp += int(new_bi[i]) * 2**(len(new_bi)-1-i)
        answer.append(tmp)               
        
    return answer
