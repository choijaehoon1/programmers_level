def solution(files):
    answer = []
    result = []
    cnt = 0
    for file in files:
        # print(file)
        cnt += 1
        head,number = '',''
        idx = 0
        for i in range(len(file)):
            if file[i].isnumeric():
                idx = i
                break
        head = file[:idx].lower()
        number = file[idx]
        for i in range(idx+1,len(file)):
            if not file[i].isnumeric():
                break
            else:
                number += file[i]
        
        result.append([head,int(number),cnt,file])
    # print(result)                    
    result.sort(key = lambda x:(x[0],x[1],x[2]))
    for i in result:
        answer.append(i[3])
                
    return answer
