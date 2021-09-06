

def solution(lines):
    # lines = S T
    # YYYY-MM-DD hh:mm:ss.sss 0.000s
    # 응답완료시간 처리시간, 처리시간은 3초 이내
    # 응답완료시간을 기준으로 오름차순 정렬
    logs = []

    for i in lines:
        # logs += [[int(x[:1])*3600000 + int(x[3:5])*60000 + int(x[6:8])*1000 + int(x[9:]), int(y[:-1])] \
        #         for _, x, y in i.split()]
        ## WHY ?
        _, x, y = i.split()
        logs.append([int(x[:2])*3600*1000 + int(x[3:5])*60*1000 + int(x[6:8])*1000 + int(x[9:]), int(float(y[:-1])*1000)])

    
    print(logs) ##
    
    stpoint = [i[0]-i[1]+1 for i in logs]

    timeset = []
    for i in logs:
        timeset.append((i[0]-i[1]+1, i[0]))
    
    # print(f"TIMESET {timeset}") ## 


    ret = 0
    for i in stpoint:
        temp = 0
        for j in timeset:
            if comp((i-999, i), j):
                temp+=1
        if temp > ret:
            print(i) ##
            ret = temp
    
    return ret

def comp(a, b):
    a1, a2 = a[0], a[1]
    b1, b2 = b[0], b[1]
    if b1<=a1<=b2 or b1<=a2<=b2 or b1<=a1<=a2<=b2 or a1<=b1<=b2<=a2:
        return True

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))