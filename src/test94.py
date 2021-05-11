import math
def solution(n, m):
    answer = [0,0]
    max_n = math.gcd(n,m)
    
    n = n // max_n
    m = m // max_n
    min_n = n*m*max_n
    answer[0] = max_n
    answer[1] = min_n
    
    return answer
