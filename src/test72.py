import math

def check(n):
    num = math.sqrt(n)
    check_num = int(num)
    
    if check_num == num:
        return num
    return False

def solution(n):
    answer = -1
    result = check(n)
    if result != False:
        answer = math.pow(result+1,2)
    
    return answer
