# 내가 짠 dfs 방식의 코드 
def solution(land):
    answer = 0
    direction=[[0,1],[0,-1],[1,0],[-1,0]]
    for x in range(len(land[0])):
        c_list=set([])
        c2_list=[]
        for y in range(len(land)):
            if land[y][x]==1 and (y,x) not in c_list:
                c_list.add((y,x))
                c2_list.append([y,x])
                while c2_list:
                    new_y,new_x=c2_list.pop()
                    for dx,dy in direction:
                        if (new_y+dy,new_x+dx) not in c_list:
                            if 0<=new_y+dy<len(land) and 0<=new_x+dx<len(land[0]) and land[new_y+dy][new_x+dx]==1:
                                c2_list.append([new_y+dy,new_x+dx])
                                c_list.add((new_y+dy,new_x+dx))
        answer=max(len(c_list),answer)
    return answer

#dfs시 효율성 오류가 나서 bfs로 변환하는 부분 검색하여 바뿐 부분
from collections import deque
def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    result = [0 for i in range(m+1)]
    visited = [[0 for i in range(m)] for j in range(n)]
    def bfs(a, b):
        count = 0
        visited[a][b] = 1
        q = deque()
        q.append((a,b))
        min_y, max_y = b, b
        while q:
            x,y = q.popleft()
            min_y = min(min_y, y)
            max_y = max(max_y, y)
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
        
        for i in range(min_y, max_y+1):
            result[i] += count
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and land[i][j] == 1:
                bfs(i,j)
    answer = max(result)
    return answer