from itertools import permutations
def solution(numbers):
    answer = '0'
    n = len(numbers)
    for i in permutations(numbers):
        temp = ''
        for j in i:
            temp+=str(j)
        if temp[0] == 0:
            temp = temp[1:]
        if int(answer) < int(temp):
            answer = temp
        
    return answer

def comp(ans, tar):
    if len(ans) < len(tar):
        return True
    elif len(ans) > len(tar):
        return False
    else:
        for i in range(len(ans)):
            if int(ans[i]) > int(tar[i]):
                return False
        return True