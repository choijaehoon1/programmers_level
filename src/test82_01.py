# 시간초과
import sys
sys.setrecursionlimit(10**6)
def solution(s):
    answer = 0
    
    new_s = list(s)
    for i in range(1,len(new_s)):
        if new_s[i-1] == new_s[i]:
            idx = i
            new_s[idx-1] = ''
            new_s[idx] = ''
            break
                
    tmp = ''.join(new_s)
    if tmp == '':
        return 1
    elif tmp != s:
        return solution(tmp)

    return 0    
