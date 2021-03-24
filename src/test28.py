def solution(phone_book):
    # 범위가 커서 터지므로 유사한 번호가 오게 정렬 후 다음값과 비교 
    phone_book.sort() # O(N Log N)
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]: # 안에 들어가 있는 형태
            if phone_book[i+1].index(phone_book[i]) == 0: # i+1번째에서 i번째 인덱스를 찾는데 접두어인지 check
                return False
    return True
