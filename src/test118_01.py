# 시간초과 10,11
def binary(n):
    tmp = ''
    while n > 0:
        t = n % 2 
        tmp = str(t) + tmp
        n //= 2
    return tmp

def check(bi01,bi02):
    cnt = 0
    for i in range(len(bi01)):
        if bi01[i] != bi02[i]:
            cnt += 1
        if cnt >=3:
            return False
    if cnt <= 2:
        return True

def solution(numbers):
    answer = []
    for number in numbers:
        bi01 = binary(number)
        while True:
            number += 1
            bi02 = binary(number)
            cnt = 0
            if len(bi01) < len(bi02):
                cnt = len(bi02) - len(bi01)
            
            for i in range(cnt):
                bi01 = '0' + bi01
                
            if check(bi01,bi02):
                answer.append(number)
                break
        
        
    return answer
