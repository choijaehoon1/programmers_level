import math
def solution(brown, yellow):
    answer = [0,0]
    total = brown + yellow
    width, height = 0, 0
    
    for i in range(1, total+1):
        if total % i == 0: # 전체에서 높이로 나누어 질때만 확인
            height = i 
            width = total // i
            # 노란색 가로는 갈색 가로-2, 노란색 세로는 갈색 세로-2이고 가로가 세로보다 크거나 같을때 갱신
            if (width-2)*(height-2) == yellow and width >= height: 
                answer[0] = width
                answer[1] = height
    return answer
