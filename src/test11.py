def solution(skill, skill_trees):
    answer = 0
    
    for i in skill_trees:
        flag = True
        index = 0
        for j in i:
            if j in skill:
                if j == skill[index]:
                    index+=1
                else:
                    flag = False
        if flag == True:
            answer+=1
    
    return answer
