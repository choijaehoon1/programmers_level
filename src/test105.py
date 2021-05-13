def solution(record):
    answer = []
    data = {}
    for r in record:
        tmp = r.split()
        if tmp[0] == 'Enter':
            data[tmp[1]] = tmp[2]
        elif tmp[0] == 'Change': 
            data[tmp[1]] = tmp[2]
    
    for i in record:
        tmp = i.split()
        name = data[tmp[1]]
        
        if tmp[0] == 'Enter':
            answer.append(name + '님이 들어왔습니다.')
        elif tmp[0] == 'Leave': 
            answer.append(name + '님이 나갔습니다.')
            
    return answer
