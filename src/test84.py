from itertools import permutations
import copy
def solution(expression):
    answer = 0
    e_list = list(expression)
    n_list = []
    tmp = ''
    for i in e_list:
        if i.isnumeric():
            tmp += i
        else:
            n_list.append(int(tmp))
            n_list.append(i)
            tmp = ''
    n_list.append(int(tmp))
    # print(n_list)        
        
    check = []
    if '-' in expression:
        check.append('-')
    if '+' in expression:
        check.append('+')
    if '*' in expression:
        check.append('*')
    combi_list = list(permutations(check,len(check)))
    # print(combi_list)
                    
    for combi in combi_list:
        new_list = copy.deepcopy(n_list)
        for c in combi:
            if c in new_list[:]:
                while c == '-' and c in new_list:
                    idx = new_list.index(c)
                    num = new_list[idx-1] - new_list[idx+1]
                    del new_list[idx+1]
                    del new_list[idx]
                    del new_list[idx-1]
                    new_list.insert(idx-1,num)
                    
                while c == '+' and c in new_list:
                    idx = new_list.index(c)
                    num = new_list[idx-1] + new_list[idx+1]
                    del new_list[idx+1]
                    del new_list[idx]
                    del new_list[idx-1]
                    new_list.insert(idx-1,num)
                    
                while c == '*' and c in new_list:
                    idx = new_list.index(c)
                    num = new_list[idx-1] * new_list[idx+1]
                    del new_list[idx+1]
                    del new_list[idx]
                    del new_list[idx-1]
                    new_list.insert(idx-1,num)                    
        if new_list != []:                    
            answer = max(answer,abs(new_list[0]))
                    
    return answer
