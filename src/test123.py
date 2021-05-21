def trans(song):
    
    song = song.replace('C#','c')
    song = song.replace('D#','d')        
    song = song.replace('F#','f')                
    song = song.replace('G#','g')                        
    song = song.replace('A#','a')                                
    
    return song        
        

def solution(m, musicinfos):
    answer = ''
    
    result = []
    music_id = 0
    for music in musicinfos:
        music_id += 1
        start,end,title,song = music.split(',')
        s_h,s_m = start.split(':')
        e_h,e_m = end.split(':')
        hh = int(e_h) - int(s_h)
        
        if hh == 0:
            play_time = int(e_m) - int(s_m)
        else:            
            play_time = hh * 60 + int(e_m) - int(s_m)
        
        m = trans(m)
        new_song = trans(song)
        
        length = len(new_song)
        total_song = ''
        if length >= play_time:
            total_song = new_song[:play_time]
        elif length < play_time:
            cnt = play_time // length
            res = play_time % length    
            total_song = new_song * cnt + new_song[:res]               
        
        for i in range(len(total_song)):
            combi = total_song[i:i+len(m)]
            if m == combi:
                result.append([play_time,music_id,title])
        
    if result == []:
        return "(None)"
    
    result.sort(key = lambda x:(-x[0],x[1]))        
    answer = result[0][2]
    return answer 
        
    
