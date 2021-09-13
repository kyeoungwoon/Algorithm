def solution(n, k, cmd):
    # U X : X칸 위 선택 (D는 아래)
    # C : 현재 행 삭제 후 아래 행 선택 (마지막 행이였을 경우 윗 행 선택)
    # Z : 가장 마지막에 선택된 행 복구, 현재 선택된 행은 바뀌지 않음
    # 처음 표의 행의 개수 n, 처음 선택된 행 k, 명령어 cmd

    # 표에서 절대적인 위치와 상대적인 위치를 알려주는 변수가 따로 필요함

    ## 1차 틀린 이유 : Z 명령어가 연속되서 나올 경우를 대비하지 못함. 마지막 하나만 리스트에 저장했던 탓.
    ## 테스트도 통과하지 못함. 시간초과

    ## 2차 코드. 효율성 테스트 8 뺴고 통과, 업 다운을 통합하여서 한번에 계산하도록 구현했음. 여기서 더 어떻게 줄이지?
    ## cm.split()을 사용하지 않고 cm[0], cm[2:]로 사용 가능 / 의미있는 차이 없음
    ## 
    

    global ret 
    ret = [True for _ in range(n)]
    last = []
    relCur = k
    absCur = k
    relN = n-1

    temp = 0

    for cm in cmd:
        cm = cm.split()
        if cm[0] == 'C': # 현재 행 삭제, 절대위치 참조헤서 X 변경, 절대위치 상대위치 모두 +1 (마지막 행일 경우 -1)
            absCur = move(absCur, temp)
            relCur+=temp
            temp = 0

            ret[absCur] = False
            last.append(absCur)

            if relCur == relN:
                absCur = move(absCur, -1)
                relCur-=1
            else:
                absCur = move(absCur, 1)
            relN-=1

            # print(f"absCur {absCur} relcCur {relCur} relN {relN} ret {ret}") ##
        
        elif cm[0] == 'Z': # 롤백, 현재 위치보다 앞의 것이 롤백될 경우 상대위치가 밀려야 함
            absCur = move(absCur, temp)
            relCur+=temp
            temp = 0

            ret[last[-1]] = True
            if absCur > last[-1]:
                relCur+=1
            last.pop()
            relN+=1

            # print(f"absCur {absCur} relcCur {relCur} relN {relN} ret {ret}") ##
        elif cm[0] == 'U':
            temp -= int(cm[1])
        elif cm[0] == 'D':
            temp += int(cm[1])

    ret_ = ''
    for i in ret:
        if i:
            ret_+='O'
        else:
            ret_+='X'
            
    return ret_

def move(cur, k):

    if k>0:
        sign = 1
    elif k<0:
        sign = -1
    else:
        return cur

    trial = 0
    while trial != k: ## 이 부분을 개선해야 하는데 연결리스트로 다음 노드를 바로 알려주는게 아닌 이상 답이 없는데
        cur+=sign
        if ret[cur]:
            trial+=sign

    return cur

ans = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
print(ans)