# 입실 퇴실

def solution(enter, leave):

    ppl = len(enter)
    enter, leave = enter[::-1], leave[::-1]
    room = []
    ret = [set() for _ in range(ppl)]
    
    nextEnter = enter.pop()
    nextLeave = leave.pop()

    while enter or leave:
        if nextLeave in room:
            room.remove(nextLeave)
            if leave: nextLeave = leave.pop()
            else: nextLeave = None
        else:
            room.append(nextEnter)
            if enter: nextEnter = enter.pop()
            else: nextEnter = None

        for i in room:
            for j in room:
                ret[i-1].add(j)
            
    for n, i in enumerate(ret):
        if i: ret[n] = len(i)-1
        else: ret[n] = 0
        
    return ret


"""
[1, 4, 2, 3] [2, 1, 3, 4] []
[4, 2, 3] [2, 1, 3, 4] [1]
[2, 3] [2, 1, 3, 4] [1, 4]
[3] [2, 1, 3, 4] [1, 4, 2]
[3] [1, 3, 4] [1, 4]
[3] [3, 4] [4]
[] [3, 4] [4, 3]
[] [4] [4]
[] [] []
"""