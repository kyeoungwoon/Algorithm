import time

def solution(s):
    round, zrA = 0, 0

    while True:
        if s == '1':
            break

        # print(f"BEFORE {s}, {zrA}") ##
        s, zr = bivert(s)
        round += 1
        zrA += zr
        # print(f"AFTER {s} | {round} {zrA}") ##
        # time.sleep(2)
        
    return [round, zrA]


def bivert(n):
    # n = [i for i in n]
    zr = 0
    for i in n:
        if i == '0': ## 이 미친새끼야 str이랑 int랑 비교를 처 떄리고 있냐 ^ㅣ
            zr+=1
    # n = ''.join(n)
    n = format(len(n)-zr, "b")
    # print(f"FUNC {n} {zr}") ##

    return (n, zr)

# solution("110010101001")