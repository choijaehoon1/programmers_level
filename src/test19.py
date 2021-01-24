def solution(number, k):
    answer = ''
    num = list(number)
    stack = [num[0]] 
    
    cnt = 0
    for i in range(1,len(num)): # 초기값 0번째는 setting 했으므로 2번째부터 비교
        if cnt == k:
            stack += num[i:] # 제외했으므로 나머지연산은 더하지 않고 뒤에부분 붙여서 중단
            break
        
        stack.append(num[i]) # 일단 하나씩 넣고 조건 빅
        
        if stack[-1] > stack[-2]: # 마지막에 들어온 스택의 값이 이전의 값보다 클때만 비교
            while len(stack) != 1 and stack[-1] > stack[-2] and cnt < k:
                stack[-1],stack[-2] = stack[-2],stack[-1]
                stack.pop()
                cnt += 1
    answer = ''.join(stack[:len(num)-k]) # 전체길이에서 k만큼 제외한 자리수가 answer 이다.
        
    return answer
