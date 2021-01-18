
def solution(bridge_length, weight, truck_weights):
    on_bridge = [0]*bridge_length # 다리의 길이만큼 0으로 초기화작업
    time = 0
    
    while on_bridge:
        time += 1        
        on_bridge.pop(0) # 시간이 증가할때마다 다리에 있는 트럭들을 하나씩 제거
        if truck_weights: # 대기트럭이 있으면
            if sum(on_bridge) + truck_weights[0] <=weight:
                on_bridge.append(truck_weights.pop(0)) 
            else:
                on_bridge.append(0) # 조건에 만족하지 않으면 0을 삽입
        
    return time
