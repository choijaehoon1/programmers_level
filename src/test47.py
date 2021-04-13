def solution(s):
    s = s.lower()
    
    table = [0,0]
    table[0] = s.count('p')
    table[1] = s.count('y')
    
    if table[0] == table[1]:
        return True
    else:
        return False
