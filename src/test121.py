from collections import deque
def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        answer += len(cities)*5
    else:
        cache_list = deque()
        idx = 0
        if len(cache_list) < cacheSize:
            for i in range(len(cities)):
                if cities[i].lower() in cache_list:
                    tmp = cache_list.index(cities[i].lower())
                    del cache_list[tmp]
                    cache_list.appendleft(cities[i].lower())
                    answer += 1
                else:                    
                    cache_list.appendleft(cities[i].lower())
                    answer += 5
                
                if len(cache_list) >= cacheSize:
                    idx = i
                    break
        
        for i in range(idx+1,len(cities)):
            if cities[i].lower() not in cache_list:
                cache_list.pop()
                answer += 5 
                cache_list.appendleft(cities[i].lower())
            elif cities[i].lower() in cache_list:
                tmp = cache_list.index(cities[i].lower())
                del cache_list[tmp]
                cache_list.appendleft(cities[i].lower())
                answer += 1
            
    return answer
