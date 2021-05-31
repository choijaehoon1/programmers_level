def solution(n, times):
    answer = 0
    
    start = 0
    end = max(times)*n # 최악의 경우(심사 가장 오래걸리는 사람한테 모두 다 받는 경우)
    
    while start <= end:
        mid = (start+end) // 2 # 심사받는데 걸리는 총 시간
        possible = 0
        for i in times:
            possible += mid // i # 각 심사관한테 받을 수 있는 가능한 심사인원의 수
            
            if possible >= n: # 주어진 사람들 이상으로 검사했으면 break
                break
        
        if possible >= n: # 심사를 더 많이한 경우 총 시간을(범위) 줄여봄
            answer = mid
            end = mid -1
        else:
            start = mid + 1 
    
    return answer
