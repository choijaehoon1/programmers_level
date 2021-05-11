def solution(strings, n):
    answer = []
    result = []
    for i in range(len(strings)):
        result.append([strings[i][n],strings[i]])
    
    result.sort(key = lambda x:(x[0],x[1]))
    # print(result)
    for i in result:
        answer.append(i[1])

    return answer
