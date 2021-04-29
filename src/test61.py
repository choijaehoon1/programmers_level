import math
def solution(w,h):
    answer = 0
    total = w*h
    
    if w == h:
        answer =total - w
    else:
        num = math.gcd(w,h)
        answer = total - (w+h-num)
    
    return answer
