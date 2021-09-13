# 입실 퇴실

# 1차 : 테스트26, 27 시간초과 FAIL
# 2차 : PASS

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
            for i in room:
                ret[nextEnter-1].add(i)
                ret[i-1].add(nextEnter)
            room.append(nextEnter)

            if enter: nextEnter = enter.pop()
            else: nextEnter = None
            
    for n, i in enumerate(ret):
        ret[n] = len(i)
        
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