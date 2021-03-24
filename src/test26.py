def solution(name):
    answer = 0
    # 오른쪽으로 이동해서 찾는 경우와 Z로 한번 이동 후 차이만큼 더한 것 작은 값이 최소비용
    dp = []
    for i in name:
        dp.append(min(ord(i)-ord('A'), ord('Z') - ord(i) + 1))
    
    idx = 0
    while True:
        # 위아래 방향일 때 값 더해주고 테이블 초기화
        answer += dp[idx] 
        dp[idx] = 0 
        
        if sum(dp) == 0:
            break
        
        left_idx = 1 # 왼쪽으로 한칸
        right_idx = 1 # 오른쪽으로 한칸
        # 인덱스가 A인 경우 좌우방향 그리디 탐색
        # EX) 다음이나 이전 문자가 A일때 오른쪽으로 두번이동하는 것보다 왼쪽으로 한번이동하는 것이 효율적
        while dp[idx-left_idx] == 0: 
            left_idx += 1
        while dp[idx+right_idx] == 0:
            right_idx += 1    
        
        # 최솟값을 더한 후 인덱스 조정
        if right_idx > left_idx: # 왼쪽으로 이동하는 경우가 더 비용이 작은 경우
            answer += left_idx 
            idx -= left_idx # 인덱스 조정
        elif right_idx <= left_idx: # 오른쪽으로 이동하는 경우가 비용이 더 작거나 같은 경우
            answer += right_idx
            idx += right_idx # 인덱스 조정
    return answer
