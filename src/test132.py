import math
def solution(arr):
    answer = 0
    
    lcm = arr[0]
    for i in range(1,len(arr)):
        gcd = math.gcd(lcm,arr[i])
        res01 = lcm // gcd
        res02 = arr[i] // gcd
        lcm = gcd * res01 * res02
        answer = lcm
         
    
    return answer
