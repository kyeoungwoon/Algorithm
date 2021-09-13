def solution(s):
    st = s[0]
    idx = [x for x, y in enumerate(s) if y == st]
    space = set()
    for i in range(1,len(idx)):
        space.add(idx[i]-idx[0])

    ret = []

    for sp in space:
        res = ''
        rpt = len(s)//sp - 1
        piece = [s[sp*i:sp*(i+1)] for i in range(rpt)] + [s[sp*rpt:]]
        print(f"PIECE {piece}") ##
        
        i=0
        while i < len(piece)-1:
            temp = 1
            while i+temp < len(piece) and piece[i] == piece[i+temp]:
                temp+=1
            res += piece[i]
            if temp > 1:
                res += str(temp)
            i+=temp

        print(res) ##
        ret.append(len(res))
    
    print(ret) ##
        
    return min(ret)

solution("aabbaccc")