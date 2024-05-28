from collections import deque

def check(x, y, board, visited):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
    possible_paths = []
    for dx, dy in directions:
        new_x, new_y = x, y
        while True:
            next_x, next_y = new_x + dx, new_y + dy
            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]) and board[next_x][next_y] != 'D':
                new_x, new_y = next_x, next_y
            else:
                break
        if (new_x, new_y) not in visited:
            possible_paths.append((new_x, new_y))
            visited.add((new_x, new_y))
    return possible_paths

def solution(board):
    # 시작점과 목표점 찾기
    start = goal = None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)
    
    if not start or not goal:
        return -1
    
    visited = set([start])
    queue = deque([(start[0], start[1], 0)])  # (x, y, 거리)
    
    while queue:
        x, y, distance = queue.popleft()
        if (x, y) == goal:
            return distance
        for new_x, new_y in check(x, y, board, visited):
            queue.append((new_x, new_y, distance + 1))
    
    return -1