def solution(name):
    answer = 0
    min_move = len(name) - 1  # 최소 좌우 이동 횟수 초기화
    # min_move는 이전까지 계산된 최소 이동 횟수
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)  # 상하 조작 횟수 더하기
        
        #i는 현재 위치, next는 'A'가 아닌 다음 문자까지의 거리
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 현재 위치에서 다시 되돌아가는 경우와 계속 진행하는 경우 중 더 짧은 이동 거리 계산
        # i + len(name) - next는 직진이동거리
        min_move = min(min_move, i + len(name) - next + min(i, len(name) - next))
        print(i + len(name) - next , min(i, len(name) - next))
    print(min_move)
    answer += min_move
    return answer
