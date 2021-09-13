from collections import Counter

def solution(weights, records):
    
    info = []
    num = 0
    for weight, record in zip(weights, records):
        win, lose, win_heavier = 0, 0, 0
        player_weight = weights[num]
        for pnum, rec in enumerate(record):
            if rec == 'W':
                win += 1
                if weights[pnum] > player_weight:
                    win_heavier += 1
            elif rec == 'L':
                lose+=1
        if win or lose: winrate = float(win / (win+lose))
        else: winrate = float(0)
        info.append([num, winrate, win_heavier, weight])
    info.sort(key=lambda x:x[1])
    info.sort(key=lambda x:x[2])
    info.sort(key=lambda x:x[3])
    info.sort(key=lambda x:x[0])

    ret = []
    for i in info:
        ret.append(i[0])

    return ret

# 선수번호, 승률, 자신보다 무거운 사람 이긴 횟수, 몸무게, (선수 번호)

test = solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])
print(test)