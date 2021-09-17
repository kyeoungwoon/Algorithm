# 퍼즐 조각 채우기
# idea : 행렬, 행렬의 회전


import numpy as np

def solution(board, table):

    board, table = np.array(board), np.array(table)
    size = len(board)-1
    
    board_piece, table_piece = [], []
    


    return

def rotate(org): return np.array(list(zip(*org[::-1]))) # 우측으로 90도 회전

def find(board):
    visited = board
    size = len(board)-1
    x, y = 0, 0

    while not board[y][x]:
        if x == size:
            y += 1
            x = 0
        x+=1

    move = [[0, 1, 0, -1], [-1, 0, 1, 0]] # 상하좌우

    for mx, my in zip(*move):
        nx, ny = x+mx, y+my
        if 0 <= nx <= size and 0 <= ny <= size:
            if not visited[ny][nx]:
                visited[ny][nx] = 1 







ans = solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
                [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]])
print(ans)
