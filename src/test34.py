from collections import defaultdict
from itertools import combinations
def solution(info, query):
    answer = []
    info_dict = defaultdict(list) # 키에 대한 값저장하는 리스트형태으 딕셔너리 선언
    for i in info:
        info_list = i.split()
        info_key = info_list[:-1] # 키부분 
        info_value = int(info_list[-1]) # 값
        for k in range(5): # k는 0(아무질의가 없는 형태) ~ 4(언어,직군,경력,소울푸드) 조합 형태
            combi_list = list(combinations(info_key,k))
            for c in combi_list: # 키의 조합을 만들고 하나씩 추출
                tmp = ''.join(c) # 하나의 키 리스트를 문자열로 결합하여 키문자 생성
                info_dict[tmp].append(info_value) # 딕셔너리에 키,값 형태로 저장
    
    for key in info_dict.keys():
        info_dict[key].sort() # 이분탐색을 위해 값들 오름차순으로 정렬
    # print(info_dict)            
    
    for q in query: 
        q_list = q.split()
        q_key = q_list[:-1] # list 형태임
        q_value = int(q_list[-1])
        
        while "and" in q_key:
            q_key.remove("and") # list형태이므로 remove함수 사용 가능
        
        while '-' in q_key:
            q_key.remove('-') # list형태이므로 remove함수 사용 가능           
        
        new_query = ''.join(q_key) # 쿼리리스트를 키문자로 변환
        if new_query in info_dict: # 키에 해당하는 값이 있을 때
            scores = info_dict[new_query] # scores 키에 해당하는 값을 담은 리스트
            if len(scores) > 0: # 값이 1개이상일 때 이분탐색 수행
                start = 0
                end = len(scores)
                
                while start < end:
                    mid = (start + end)//2
                    if scores[mid] >= q_value:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start) # start인덱스부터 마지막까지는 ~~점이상 받은 지원자의 수임
        else: # 해당하는 키가 없을 때는 0
            answer.append(0)
    
    return answer
