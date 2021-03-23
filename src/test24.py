from itertools import permutations
import math
# 소수찾기 함수
def find(num):
    if num < 2:
        return False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False
    return True    

def solution(numbers):
    answer = 0
    tmp_list = []
    for i in range(1,len(numbers)+1): # numbers는 최소 1개이상 문자열이므로
        tmp = list(permutations(list(numbers),i)) # 가능한 case만들기
        for j in tmp:
            tmp_list.append(''.join(j)) # 문자열로 만들어서 append
    possible_list = list(map(int,tmp_list)) # int형으로 변환
    possible_list = set(possible_list) # 중복제거
    
    # 가능한 리스트에서 소수찾기
    for i in possible_list: 
        if find(i) == True:
            answer += 1
    
    return answer
