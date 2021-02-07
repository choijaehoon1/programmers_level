from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    answer_list = []
    for i in course:
        tmp = []
        for order in orders:
            combi_list = list(combinations(sorted(order),i))
            tmp += combi_list
        tmp_dict = Counter(tmp)
        result = tmp_dict.most_common()
        try:
            max_val = result[0][1]
            if max_val >= 2:
                for j in range(1,len(result)):
                    if result[j][1] == max_val:
                        answer_list.append(result[j][0])
                answer_list.append(result[0][0])                            
        except:
            pass
        
    answer_list.sort()
    for i in answer_list:
        answer.append(''.join(i))
    
    return answer
