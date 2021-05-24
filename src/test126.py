def trans(b_type,i):
    data = '0123456789ABCDEF'
    if i == 0:
        return '0'
    
    num = ''
    while i > 0:
        num = data[i%b_type] + num
        i //= b_type
    return num        
    

def solution(n, t, m, p):
    answer = ''
    
    total = ''
    for i in  range(t*m):
        total += trans(n,i)
    # print(total)
    
    for i in  range(p-1,t*m,m):
        answer += total[i]
    
    return answer
