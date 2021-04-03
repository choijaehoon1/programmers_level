def solution(arr):
    answer = []
    
    init = arr[0]
    answer.append(init)
    for i in range(1,len(arr)):
        if init != arr[i]:
            answer.append(arr[i])
            init = arr[i]
    
    return answer
