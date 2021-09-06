import datetime as dt
import re

def solution(lines):
    
    start = []
    
    for l in lines:
        date, time, col = l.split()
        h, m, Ss = time.split(':')
        s, ms = Ss.split('.')
        
        h, m, s, ms = int(h), int(m), int(s), int(ms)
        
        end = dt.datetime(2016, 9, 15, h, m, s, ms*1000)
        
        col = re.sub('[\.s]', '', col)
        while len(col) < 4:
            col+='0'

        #print(f"ORG. COL : {col}")
        
        col_s, col_ms = int(col[0]), int(col[1:])
        col = dt.timedelta(seconds = col_s, milliseconds = col_ms) - dt.timedelta(milliseconds = 1)

        #print(f"START : {end-col}\nEND : {end}\nCOL : {col}")
        start.append(end-col)
        start.sort()
    
    ans = 0
    
    for i in range(len(start)):
        temp = 1
        for j in range(i+1, len(start)):
            if start[j] - start[i] <= dt.timedelta(seconds = 1):
                temp+=1
            else:
                break
        if temp > ans:
            ans = temp
            
    print(ans)

    return ans