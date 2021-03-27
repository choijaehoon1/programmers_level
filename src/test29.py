def solution(citations):
    answer = 0
    # 정렬을 통해 citations[i]는 최소 인용 논문의 횟수가 됨
    citations.sort()     
    for i in range(len(citations)):
        # 인용된 논문의 횟수, 인용된 논문의 수를 비교 
        if citations[i] >= len(citations) - i:
            answer = len(citations) - i
            break
    
    return answer
