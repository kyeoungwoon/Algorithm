def solution(numbers):
    
    ret = ''
    one, two, three = [], [], []
    four = False
    # 한자리수 두자리수 세자리수 구분?
    for i in numbers:
        if i//10 == 0:
            one.append(i)
        elif i//100 == 0:
            two.append(i)
        elif i/10000 == 0:
            three.append(i)
        else:
            four = True
    
    one.sort()
    two.sort()
    three.sort()

    while len(one) or len(two) or len(three):

        for i in [one, two, three]:
            if len(i) == 0:
                i.append(-1)
        
        temp = [one[-1], two[-1]//10, three[-1]//100]

        print(f"TEMP {temp}") ##

        if max(temp) == -1:
            break

        tmp = temp.index(max(temp))

        if tmp == 0:
            ret+=str(one[-1])
            one.pop()
        elif tmp == 1:
            ret+=str(two[-1])
            two.pop()
        elif tmp == 2:
            ret+=str(three[-1])
            three.pop()
    
    return ret

print(solution([6, 10, 2]))