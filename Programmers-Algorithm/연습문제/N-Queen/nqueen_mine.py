def soulution(n):
    ret = 0


def dfs(n, cur):
    pass

    
def search(n, cur, ans):
    lane = len(cur) # 탐색 노드의 깊이
    if n == lane: # 해당 줄에서는 탐색 성공, 이전 노드를 보고 모든 탐색이 완료되었는지 확인
        if cur[-1][1] == n-1:



    ret = 0
    visited = [0 for i in range(n)]
    while True:
        if ret == n: # 경로 없음, 이전 노드로 돌아가야함
            if cur[-1][1] == n-1:
                return ans
            cur[-1] = (cur[-1][0], cur[-1][1]+1)
        if visited[ret]:
            ret+=1
            continue

        is_avail = True
        for i in cur:
            xgap = abs(i[1] - ret)
            ygap = lane - i[0]
            if xgap == 0 or ygap == 0:
                visited[ret] = 1
                is_avail = False
                break
            elif xgap == ygap:
                visited[ret] = 1
                is_avail = False
                break

        if is_avail: # 해당 노드는 불가함
            ret+=1
            continue

        # for문을 다 통과하고 나온, 가능한 노드
        cur.append((lane, ret))
        search(n, cur, ans)
    
'''

왼쪽 위부터 탐색
모든 노드를 검색해야 하므로, 깊이 우선 탐색
끝까지 간 후에 올라갔다가 다시 내려가는 방식
인자에 현재까지 가능한 노드 수를 포함한다

'''