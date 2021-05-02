import copy
def solution(arr):
    answer = [-1]
    num = min(arr)
    if len(arr) > 1:
        arr.remove(num)
        answer = copy.deepcopy(arr)
    return answer
