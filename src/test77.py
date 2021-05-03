
def score(cnt):
    if cnt >= 6:
        return 1
    elif cnt >= 5:
        return 2
    elif cnt >= 4:
        return 3
    elif cnt >= 3:
        return 4
    elif cnt >= 2:
        return 5
    return 6

def solution(lottos, win_nums):
    mask = lottos.count(0)
    # print(mask)
    if mask == 0:
        cnt = 0
        for i in lottos:
            if i in win_nums:
                cnt += 1
        num = score(cnt)                
        return [num,num]
    else:
        tmp = 0
        for i in lottos:
            if i != 0 and i in win_nums:
                tmp += 1
        
        max_num = score(tmp+mask)
        min_num = score(tmp)
        return [max_num,min_num]
                
