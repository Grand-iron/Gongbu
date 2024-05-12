from collections import deque

def bfs(graph, N):
    queue = deque([(0, 0)])
    directions = [(1, 0), (0, 1)]  # 아래쪽, 오른쪽으로 이동 가능
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 확인할 리스트
    visited[0][0] = True  # 시작 지점 방문 처리

    while queue:
        x, y = queue.popleft()
        jump = graph[x][y]  # 현재 위치에서 점프할 거리

        if jump == -1:  # 도착했을 때
            return "HaruHaru"

        for dx, dy in directions:
            nx, ny = x + dx*jump, y + dy*jump  # 점프할 새 위치 계산

            # 이동 가능 조건 검사
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return "Hing"

N = int(input())  # 보드의 크기
graph = [list(map(int, input().split())) for _ in range(N)]  # 보드 정보 입력 받기

# 보드의 가장 오른쪽 하단을 -1로 설정하여 도착 지점으로 활용
graph[N-1][N-1] = -1

print(bfs(graph, N))
