n = int(input())
area = [list(map(int, input().split())) for _ in range(n)] 

def dfs(x, y, height):
    # 범위 체크
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] or area[x][y] <= height:
        return
    visited[x][y] = True  # 현재 위치 방문 했다고 남기기
    # 상하좌우 탐색
    dfs(x+1, y, height)
    dfs(x-1, y, height)
    dfs(x, y+1, height)
    dfs(x, y-1, height)

max_safe_areas = 0
for height in range(max(map(max, area))+1):  # 물의 높이는 0부터 최대 높이까지
    visited = [[False]*n for _ in range(n)]  # 방문 여부를 기록하는 2차원 리스트 초기화
    safe_areas = 0  
    for i in range(n):
        for j in range(n):
            if area[i][j] > height and not visited[i][j]:  # 물에 잠기지 않고, 방문하지 않은 지역 탐색
                dfs(i, j, height)  # DFS로 해당 영역 탐색
                safe_areas += 1  # 안전 영역의 수 증가
    max_safe_areas = max(max_safe_areas, safe_areas)  # 최대 안전 영역의 값으로 바꾸기

print(max_safe_areas)
