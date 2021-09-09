def solution(dirs):
    cur = (0, 0)
    newLine = []
    
    for i in dirs:
        mvLoc = move(cur, i)
        if not mvLoc == cur:
            if not (mvLoc, cur) in newLine:
                newLine.append((cur, mvLoc))
            cur = mvLoc
    
    newLine = list(set(newLine))
    
    return len(newLine)
    

def move(cur, dir):
    if dir == 'U':
        if cur[1] == 5:
            return cur
        else:
            return (cur[0], cur[1]+1)

    elif dir == 'D':
        if cur[1] == -5:
            return cur
        else:
            return (cur[0], cur[1]-1)

    elif dir == 'L':
        if cur[0] == -5:
            return cur
        else:
            return (cur[0]-1, cur[1])
    
    else:
        if cur[0] == 5:
            return cur
        else:
            return (cur[0]+1, cur[1])