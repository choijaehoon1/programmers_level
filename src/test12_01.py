from collections import Counter
def solution(participant, completion):
    
    tmp_dict = Counter(participant) - Counter(completion)
    answer = tmp_dict.most_common() # 딕셔너리를 리스트로 변경
    
    return answer[0][0]
