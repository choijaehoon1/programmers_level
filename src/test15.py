def solution(answers):
    supo_1 = [1,2,3,4,5]
    supo_2 = [2,1,2,3,2,4,2,5]
    supo_3 = [3,3,1,1,2,2,4,4,5,5]
    
    supo_1_cnt = 0 
    supo_2_cnt = 0 
    supo_3_cnt = 0 
    
    for i in range(len(answers)):
        if answers[i] == supo_1[i%5]:
            supo_1_cnt+=1
        if answers[i] == supo_2[i%8]:
            supo_2_cnt+=1
        if answers[i] == supo_3[i%10]:
            supo_3_cnt+=1    
    array = []
    array.append((supo_1_cnt,1))
    array.append((supo_2_cnt,2))
    array.append((supo_3_cnt,3))
    
    max_value = max(supo_1_cnt,supo_2_cnt,supo_3_cnt)
    
    num = 0
    for i in array:
        if i[0] == max_value:
            num += 1
    
    answer = []
    if num > 1:
        for i in array:
            if i[0] == max_value:
                answer.append(i[1])
        answer.sort()
        return answer
    else:
        for i in array:
            if i[0] == max_value:
                return [i[1]]
    
