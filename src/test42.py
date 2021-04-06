def solution(s):
    answer = []
    tmp = s.split('},')

    tmp_list = []
    for i in tmp:
        if '{' or '}' in i:
            i = i.replace('{','')
            i = i.replace('}','')    
        if ',' in i:
            a = list(map(int, i.split(',')))
            tmp_list.append((a,len(a)))
        else:
            tmp_list.append(([int(i)],1))      
    tmp_list.sort(key = lambda x:x[1]) # 리스트 크기가 작은 순대로 정렬
    # print(tmp_list)           
    
    for i in tmp_list:
        for j in i[0]:
            if j not in answer:
                answer.append(j)
    
    return answer
