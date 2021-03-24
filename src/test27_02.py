def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    # 문자열은 아스키코드를 기준으로 기본적으로 오름차순 정렬함(1보다 6이 아스키코드값이 큼)
    # reverse 옵션을 줘서 6과 같은 큰수가 제일 앞으로 정렬되게 변환
    numbers.sort(key = lambda x:x*3, reverse = True) # numbers는 1000이하 이므로 xxx 3자리문자로 정렬
    tmp = ''.join(numbers) 
    answer = str(int(tmp)) # 0000와 같은 숫자가 있을 수도 있으므로 int 형변환 필요
    return answer
