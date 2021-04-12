# 모든 상황을 다 고려해줘야하는데 그러기 위해서는 시간복잡도가 너무 커지므로
# 다이나믹 프로그래밍

def solution(land):
    answer = 0

    for i in range(len(land)-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
    
    answer = max(land[len(land)-1])

    return answer
