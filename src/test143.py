
def check(time,check_list):
    cnt = 0
    start = time
    end = time + 1000
    
    for c in check_list:
        if c[0] < end and c[1] >= start:
            cnt += 1
    
    return cnt

def solution(lines):
    answer = 0
    check_list = []
    for line in lines:
        date,a,b = line.split(' ')
        a = a.split(':')
        b = float(b.replace('s','')) * 1000
        
        end = (int(a[0])*3600 + int(a[1])*60 + float(a[2])) * 1000
        start = end - b + 1
        check_list.append([start,end])
        
    for c in check_list:
        answer = max(answer, check(c[0],check_list), check(c[1],check_list))
        
    return answer
