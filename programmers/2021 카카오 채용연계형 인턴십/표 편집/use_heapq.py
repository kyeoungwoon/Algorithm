import heapq

# heapq에 대한 전반적인 이해를 시켜준 문제. 좋네

def solution(n, k, cmds):
    
    left = [-i for i in range(k)] # max heap
    right = [i for i in range(k, n)] # min heap
    deleted = []
    ret = ['O' for _ in range(n)]

    heapq.heapify(left)
    heapq.heapify(right)

    def move(temp):
        if not temp:
            return
        elif temp>0:
            for _ in range(temp):
                heapq.heappush(left, -heapq.heappop(right))
        elif temp<0:
            for _ in range(-temp):
                heapq.heappush(right, -heapq.heappop(left))

    temp = 0
    for cmd in cmds:
        cmd = cmd.split()

        if cmd[0] == 'U': temp -= int(cmd[1])
        elif cmd[0] == 'D': temp += int(cmd[1])
        
        elif cmd[0] == 'C':
            move(temp)
            temp = 0
            pop_temp = heapq.heappop(right)
            if not right:
                move(-1)
            ret[pop_temp] = 'X'
            deleted.append(pop_temp)
        
        elif cmd[0] == 'Z':
            move(temp)
            temp = 0
            recov = deleted.pop()
            ret[recov] = 'O'
            if recov > right[0]: heapq.heappush(right, recov)
            else: heapq.heappush(left, -recov)
    
        # print(f"L {left} R {right}") ## 

    return ''.join(ret)

# ans = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
# print(ans)