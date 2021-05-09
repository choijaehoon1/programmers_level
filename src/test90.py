
def binary(x):
    tmp = ''
    while x > 0:
        n = x % 2
        x //= 2
        tmp = str(n) + tmp
    return tmp
    

def solution(n, arr1, arr2):
    answer = []
    tmp_list = [['#']*n for _ in range(n)]
    new_arr1 = []
    new_arr2 = []
    for i in arr1:
        num = binary(i)
        if len(num) != n:
            cnt = n - len(num)
            for j in range(cnt):
                num = '0' + num 
        new_arr1.append(list(num))
    
    for i in arr2:
        num = binary(i)
        if len(num) != n:
            cnt = n - len(num)
            for j in range(cnt):
                num = '0' + num 
        new_arr2.append(list(num))

    for i in range(n):
        for j in range(n):
            if new_arr1[i][j] == '0':
                new_arr1[i][j] = ''
            elif new_arr1[i][j] == '1':
                new_arr1[i][j] = '#'
                
    for i in range(n):
        for j in range(n):
            if new_arr2[i][j] == '0':
                new_arr2[i][j] = ''
            elif new_arr2[i][j] == '1':
                new_arr2[i][j] = '#'                
    
    for i in range(n):
        for j in range(n):
            if new_arr1[i][j] == '' and new_arr2[i][j] == '':
                tmp_list[i][j] = ''
    
    for i in tmp_list:
        tmp = ''
        for j in i:
            if j == '':
                tmp += ' '
            else:
                tmp += j    
        answer.append(tmp)
            
    return answer
