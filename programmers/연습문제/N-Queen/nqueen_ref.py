def solution(n):

    global count
    global num
    global board

    count = 0
    num = n
    board = [0 for _ in range(n)]

    nqueen(0)
    print(count)

def promising(cdx):

    for i in range(cdx):
        if board[cdx] == board[i] or (cdx-i) == abs(board[cdx] - board[i]):
            return 0

    return 1

def nqueen(cdx):

    global count

    if cdx == num:
        count+=1
        return

    for i in range(num):
        board[cdx] = i
        if promising(cdx):
            nqueen(cdx+1)
    

solution(4)