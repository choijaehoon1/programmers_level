from collections import deque
# 시간복잡도 문제 1초에 100000000(1억)이하 이어야 한다.
# 해당 문제의 경우 N이 100000임  
# 만약 deque 사용안하고 pop(0)연산 사용시
# for문 O(n) pop(0)연산 시간복잡도O(n)이므로 O(n^2)이 된다.
# O(n^2)은 10000000000 백억이 되므로 시간초과 판정
# 따라서 for문 O(n)과 O(1)인 popleft() 연산을 사용하여야 함
def solution(participant, completion):
    participant.sort()
    completion.sort()
    q = deque()
    for i in completion:
        q.append(i)
    for i in participant:
        if i not in q:
            return i
        else:
            q.popleft() 
