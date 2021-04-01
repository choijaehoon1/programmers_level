# 3진법 변환 + 앞뒤 반전
def three_trans(n):
    tmp = ''
    while n > 0:
        tmp += str(n % 3)
        n = n // 3
    return tmp    

# 3진법을 다시 10진법으로 변환
def ten_trans(str_n):
    num = 0
    three = 1
    for i in range(len(str_n)-1,-1,-1):
        if str_n[i] != '0':
            num += int(str_n[i]) * three
        three *= 3            
    return num

def solution(n):
    answer = 0
    tmp = three_trans(n)    
    answer = ten_trans(tmp)
    return answer
