def solution(n):
    answer = ''
    while n > 0:
        res = n % 3
        n //= 3
        if res == 0: # 이후에는 자리수가 올라가므로 4로 설정해주고 n숫자 조정
            res = 4
            n -= 1
        answer =  str(res) + answer
    
    return answer
