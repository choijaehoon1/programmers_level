def solution(s):
    stack = []
    
    for i in s:
        if stack == []:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        elif stack[-1] != i:            
            stack.append(i)

    if stack == []:
        return 1
    else:
        return 0

