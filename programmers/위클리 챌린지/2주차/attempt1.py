# 상호 평가

def solution(scores):
    ret = ""
    totalStudent = len(scores)
    
    temp = [[] for _ in range(totalStudent)]
    for scs in scores:
        for n, sc in enumerate(scs):
            temp[n].append(sc)
    scores = temp

    for studentNum, scoreList in enumerate(scores):
        myScore = scoreList[studentNum]
        if myScore in [max(scoreList), min(scoreList)]:
            scoreList.remove(myScore)
            if myScore in scoreList:
                scoreList.append(myScore)
        average = sum(scoreList)/len(scoreList)
        ret += grade(average)
        print(scoreList, average) ##
    return ret
            

def grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 50: return 'D'
    else: return 'F'

ans = solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]])
print(ans)

# 성공, 근데 피곤해서 코드 개판으로 짯음. 추후 수정 요망.

## zip(*scores)로 행렬 뒤집을 수 있음. cool shit!