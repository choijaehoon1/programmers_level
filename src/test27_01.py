# 시간 초과
from itertools import permutations
def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    tmp_list = list(permutations(numbers,len(numbers)))
    result = []
    for i in tmp_list:
        result.append(''.join(i))
    result = list(set(list(map(int,result))))
    answer = str(max(result))
    return answer
