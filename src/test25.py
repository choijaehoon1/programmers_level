import heapq
# 가장 낮은 스코빌지수가 K보다 크거나 같은 경우는 True
def check(h,K):
    tmp = h[0]
    if tmp >= K:
        return True
    return False

def solution(scoville, K):
    answer = 0
    h = []
    for i in scoville:
        heapq.heappush(h,i)
            
    while check(h,K) == False: # 모든 지수를 스코빌지수로 만들기위해 반복 수행
        if len(h) == 0: # heap이 비어있으면 K이상 못만드므로 -1
            return -1
        if len(h) == 1: # heap의 개수가 1개인데 K보다 작으면 만들 수 없는 경우이므로 -1
            if h[0] < K:
                return -1
        # 스코빌 지수 만드는 과정            
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        heapq.heappush(h,a + 2*b)
        answer += 1
    return answer
