def solution(N, number):
    answer = 0
    
    possible = [0,[N]] # i_half에서 첫번째 인덱스 부터 시작(인덱스 맞춰주기 0추가)
    
    if N == number:
        return 1
    
    for i in range(2,9): # 2부터 8까지만 확인, 최소값이 8보다 크면 -1
        tmp = []
        base = int(str(N)*i)
        tmp.append(base)
        
        for i_half in range(1,i//2+1):  # 절반 까지만 검사(절반 이상넘어가면 똑같은거 반복 ex) 1,3과 3,1)
            for x in possible[i_half]:
                for y in possible[i-i_half]:
                    tmp.append(x+y)
                    tmp.append(x-y)
                    tmp.append(y-x)
                    tmp.append(x*y)
                    if x != 0:
                        tmp.append(y/x)
                    if y != 0:
                        tmp.append(x/y)                        
        if number in tmp:
            return i
        possible.append(tmp)
        
    return -1
