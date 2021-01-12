def solution(prices):
    answer = []
    
    for i in range(len(prices)):
        time = 0
        for j in range(i+1,len(prices)): 
            # 가격이 떨어지지 않는 기간 구하기
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)
    
    return answer
