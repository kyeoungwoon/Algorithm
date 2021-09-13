import math

def solution(prog, speed):
    left = []
    for i in range(len(prog)):
        left.append(math.ceil((100-prog[i])/speed[i]))

    print(f"LEFT {left}") ##

    ret = []
    i = 0
    
    while i < len(left):
        temp = 1
        while True:
            if i+temp == len(left):
                break
            if left[i] >= left[i+temp]:
                temp+=1
            else:
                break
        ret.append(temp)
        i+=temp
    
    return ret

solution([93, 30, 55], [1, 30, 5])

## CORRECT