import math
def solution(w,h):
    
    total = w * h
    if w == h: # 정사각형인 경우
        return total - w
    else: # 직사각형인 경우
        # 가로질러가는 가로의 개수 + 세로의 개수에서 - 최대공약수 빼주기
        # ex) 가로가 2, 세로가 3일 때 
        # 가로질러가는 가로: 3개 , 가로질러가는 세로: 2개, 최대공약수는 1
        return total - (w+h-math.gcd(w,h)) 
    
