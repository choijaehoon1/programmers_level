def solution(a, b):
    answer = ''
    num = 0
    weeks = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    for i in range(1,a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            num += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            num += 30
        else:
            num += 29
        
    num += b-1 # 24일이 몇번째 날인지 알아야 하므로 일은 1부터 시작이므로 1에다가 b-1인 23을 더해줘야함
    res = num % 7
    answer = weeks[res]
    
    return answer
