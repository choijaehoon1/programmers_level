from itertools import combinations
from collections import defaultdict
def solution(info, query):
    answer = []
    info_dict = defaultdict(list) # 타입이 list형
    # DB만들기
    for i in info:
        inf = i.split()
        inf_key = inf[:-1]
        inf_value = int(inf[-1]) # 마지막 값은 int형
        for k in range(5): # 조합은 4개 컬럼 조합까지 가능
            combi_list = list(combinations(inf_key,k))
            # print(combi_list)
            for c in combi_list: # 하나하나 키에 대해 확인
                tmp = ''.join(c)
                info_dict[tmp].append(inf_value) # 해당 키에대한 값 저장
    # print(info_dict)                
    
    for key in info_dict.keys(): 
        info_dict[key].sort() # 이분탐색을 위한 정렬
    # print(info_dict)
    
    # 쿼리 생성
    for q in query:
        quer = q.split()
        quer_key = quer[:-1]
        quer_value = int(quer[-1])
        
        for i in range(3):
            quer_key.remove("and")
        while '-' in quer_key:
            quer_key.remove('-')
        new_query = ''.join(quer_key)
        # print(new_query)
        
        if new_query in info_dict: # 쿼리가 존재하면
            scores = info_dict[new_query] # 해당 쿼리에 대한 값들
            if len(scores) > 0: # 쿼리에 해당하는 값이 1개 이상일 때
                start,end = 0, len(scores)
                while start < end:
                    mid = (start+end)//2
                    if scores[mid] >= quer_value: # 중앙값이 쿼리보다 크므로 끝범위를 재지정해서 줄이기
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores)-start) # 해당 인덱스부터 끝까지의 개수가 정답
        else: # 쿼리 없으면 0
            answer.append(0)
    
    return answer
