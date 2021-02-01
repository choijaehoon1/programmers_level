def solution(new_id):
    answer = ''
    check_list = ['-','_','.'] # 가능한 문자
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for i in new_id:
        if i.isalpha() == False and i.isnumeric() == False: # 알파벳이고 숫자가 아닌 경우에만 확인
            if i not in check_list: # 해당하지 않는 문자는 변환
                new_id = new_id.replace(i,'') # replace은 전체에서 해당하는 i를 다 바꾸는 것(주의)
    # 3단계
    new_id = list(new_id) # 리스트로 변환
    try:
        for i in range(len(new_id)-1):
            if new_id[i] == '.' and new_id[i+1] == '.':
                new_id[i] = '' 
    except:
        pass

    new_id = ''.join(new_id) # 문자열로 변환(''는 붙여지므로 삭제됨)
    # 4단계
    if new_id[0] == '.' or new_id[-1] == '.':
        tmp = list(new_id)
        if tmp[0] == '.':
            tmp[0] = ''
        if tmp[-1] == '.':
            tmp[-1] = ''
        new_id = ''.join(tmp)        
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    # 6단계            
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            tmp = list(new_id)
            tmp[-1] = ''
            new_id = ''.join(tmp) 
    # 7단계    
    if len(new_id) <=2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    answer = new_id
    return answer
