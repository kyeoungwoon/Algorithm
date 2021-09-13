def solution(pb):
    pb.sort()
    for i in range(len(pb)-1):
        for j in range(i+1, len(pb)):
            if pb[j].startswith(pb[i]):
                return False

    return True