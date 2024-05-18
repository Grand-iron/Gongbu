from collections import deque

규격=input().split()
x규격=int(규격[0])
y규격=int(규격[1])
미로=[input() for x in range(x규격)]
탐색경로=deque([[0,0,1,1]])
방문기록=set([(0,0,1)])

def check(x,y,가능성,maze):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
    가능경로=[]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # 미로 범위 안에 있고, 벽이 아닌 경우(예를 들어, 빈 공간을 '0'으로 표시)
        if (new_x,new_y,가능성) not in 방문기록:
            if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and (maze[new_x][new_y] == '0' or 가능성==1):
                if (maze[new_x][new_y] == '1' and 가능성==1) or 가능성==0:
                    가능경로.append([new_x,new_y,0])
                    방문기록.add((new_x,new_y,0))
                else:
                    가능경로.append([new_x,new_y,1])
                    방문기록.add((new_x,new_y,1))
    return 가능경로

while(탐색경로):
    x,y,가능성,거리=탐색경로.popleft()
    if x== x규격-1 and y==y규격-1:
        print(거리)
        break 
    for new_x,new_y,new_가능성 in check(x,y,가능성,미로):
        탐색경로.append([new_x,new_y,new_가능성,거리+1])

else:
    print(-1)