def solution(s):
    answer = ''
    tmp = []
    for i in s:
        tmp.append([ord(i),i])
            
    tmp.sort(key = lambda x:x[0],reverse = True)
    # print(tmp)
    for i in tmp:
        answer += i[1]
    
    return answer
