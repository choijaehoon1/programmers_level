import heapq
def solution(A,B):
    answer = 0
    
    max_heap = []
    min_heap = []
    
    for i in range(len(A)):
        heapq.heappush(min_heap,A[i])
        heapq.heappush(max_heap,-B[i])
    
    while min_heap:
        a = heapq.heappop(min_heap)
        b = heapq.heappop(max_heap)
        b *= -1
        answer += a*b
    
    return answer
