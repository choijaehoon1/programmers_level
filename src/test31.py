def solution(clothes):
    answer = 1
    # Idea: database 개념, 키와 values 
    clothes_dict = {}
    for i in clothes:
        if i[1] in clothes_dict: # 해당 하는 키가 있을 경우 해당 키의 값을 더하기
            clothes_dict[i[1]].append(i[0])
        else: # 해당 키가 없으면 키에 해당하는 값 지정
            clothes_dict[i[1]] = [i[0]]
    # print(clothes_dict)
    
    # for i in clothes_dict.values():
    #     answer *= (len(i)+1)
    for i in clothes_dict.keys(): # key를 추출해서 로직 수행
        answer *= (len(clothes_dict[i])+1)
    
    return answer - 1 # 모두 안 입은 경우 제외
