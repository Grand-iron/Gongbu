from collections import deque
방문기록=set([(0,0,1)])
탐색경로=deque([[0,0,1]])
def check(x,y,maze):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
    가능경로=[]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # 미로 범위 안에 있고, 벽이 아닌 경우(예를 들어, 빈 공간을 '1'으로 표시)
        if (new_x,new_y) not in 방문기록:
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 1:
                가능경로.append([new_x,new_y])
                방문기록.add((new_x,new_y))            
    return 가능경로
        
def solution(maps):
    while(탐색경로):
        x,y,거리=탐색경로.popleft()
        if x== len(maps)-1 and y==len(maps[0])-1:
            return(거리)
        for new_x,new_y in check(x,y,maps):
            탐색경로.append([new_x,new_y,거리+1])

    else:
        return(-1)
        