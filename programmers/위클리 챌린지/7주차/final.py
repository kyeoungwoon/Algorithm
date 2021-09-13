def solution(enter, leave):

    enter, leave = enter[::-1], leave[::-1]
    room = []
    ret = [set() for _ in enter]
    
    nextEnter, nextLeave = enter.pop(), leave.pop()

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

    for n, i in enumerate(ret): ret[n] = len(i)
        
    return ret