def solution(skill, skill_trees):
    answer = 0
    new_skill = []
    for s in skill_trees:
        tmp = ''
        for i in s:
            if i in skill:
                tmp += i               
        new_skill.append(tmp)                     
    # print(new_skill)            
    
    for i in new_skill:
        flag = False
        for j in i:
            o_idx = skill.index(j)
            n_idx = i.index(j)
            if o_idx != n_idx:
                flag = True
                break
        if flag == False:
            answer += 1
    
    return answer
