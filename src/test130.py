def solution(arr1, arr2):
    f_r = len(arr1)
    f_c = len(arr1[0])
    s_r = len(arr2)
    s_c = len(arr2[0])
    
    answer = [[0]*s_c for _ in range(f_r)]
    
    arr2 = list(zip(*arr2))
    
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            tmp = 0
            for x in range(len(arr1[i])):
                tmp += arr1[i][x] * arr2[j][x]          
            result.append(tmp)
    # print(result)            
    cnt = 0            
    for i in range(f_r):
        for j in range(s_c):
            answer[i][j] = result[cnt]
            cnt+=1
    
    return answer
