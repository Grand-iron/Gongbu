from collections import deque

def bfs(x, y, graph, visited):
    n = len(graph)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동, 남, 서, 북
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1  # 시작점도 count에 포함

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n:  # 범위 체크
                if graph[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True
                    count += 1

    return count

def solution(graph):
    n = len(graph)
    visited = [[False] * n for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                result.append(bfs(i, j, graph, visited))

    result.sort()
    return result

# 입력 받기
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

# 결과 계산 및 출력
result = solution(graph)
print(len(result))
for count in result:
    print(count)
