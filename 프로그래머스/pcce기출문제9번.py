
def solution(board, h, w):
    answer = 0
    a=board[h][w]
    if h-1>=0:
        if board[h-1][w]==a:
            answer+=1
    if h+1<len(board):
        if board[h+1][w]==a:
            answer+=1
    if w-1>=0:
        if board[h][w-1]==a:
            answer+=1
    if w+1<len(board[0]):
        if board[h][w+1]==a:
            answer+=1
    return answer