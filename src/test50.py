def solution(s):
    
    if not (len(s) == 4 or len(s) == 6):
        return False
    
    for i in s:
        if i.isnumeric() == False:
            return False
    return True
