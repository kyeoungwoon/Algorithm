def solution(n, k, cmd):
    # U X : X칸 위 선택 (D는 아래)
    # C : 현재 행 삭제 후 아래 행 선택 (마지막 행이였을 경우 윗 행 선택)
    # Z : 가장 마지막에 선택된 행 복구, 현재 선택된 행은 바뀌지 않음
    # 처음 표의 행의 개수 n, 처음 선택된 행 k, 명령어 cmd

    # 표에서 절대적인 위치와 상대적인 위치를 알려주는 변수가 따로 필요함

    ## 1차 틀린 이유 : Z 명령어가 연속되서 나올 경우를 대비하지 못함. 마지막 하나만 리스트에 저장했던 탓.
    ## 테스트도 통과하지 못함. 시간초과
    

    global ret 
    ret = ['O' for _ in range(n)]
    last = []
    relCur = k
    absCur = k
    relN = n-1

    for cm in cmd:
        cm = cm.split()
        if cm[0] == 'C': # 현재 행 삭제, 절대위치 참조헤서 X 변경, 절대위치 상대위치 모두 +1 (마지막 행일 경우 -1)
            ret[absCur] = 'X'
            last.append(absCur)

            if relCur == relN:
                absCur = move(absCur, -1)
                relCur-=1
            else:
                absCur = move(absCur, 1)
            relN-=1

            # print(f"absCur {absCur} relcCur {relCur} relN {relN} ret {ret}") ##
        
        elif cm[0] == 'Z': # 롤백, 현재 위치보다 앞의 것이 롤백될 경우 상대위치가 밀려야 함
            ret[last[-1]] = 'O'
            if absCur > last[-1]:
                relCur+=1
            last.pop()
            relN+=1

            # print(f"absCur {absCur} relcCur {relCur} relN {relN} ret {ret}") ##

        # 위아래로 이동, 절대위치는 함수 따라 이동, 상대위치는 그대로 이동
        elif cm[0] == 'U': 
            cm[1] = int(cm[1])
            absCur = move(absCur, cm[1]*(-1))
            relCur-=cm[1]

            # print(f"absCur {absCur} relcCur {relCur} relN {relN} ret {ret}") ##
        
        elif cm[0] == 'D':
            cm[1] = int(cm[1])
            absCur = move(absCur, cm[1])
            relCur+=cm[1]

            # print(f"absCur {absCur} relcCur {relCur} relN {relN} ret {ret}") ##

    return ''.join(ret)

def move(cur, k):

    global ret

    if k > 0:
        trial = 0
        while trial != k:
            cur+=1
            if ret[cur] == 'O':
                trial+=1
    else:
        trial = 0
        while trial != k:
            cur-=1
            if ret[cur] == 'O':
                trial -= 1

    return cur

# ans = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
# print(ans)