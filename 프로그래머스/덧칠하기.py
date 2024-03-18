def solution(n, m, section):
    answer = 0
    x = 0
    while x < len(section):
        if x+1 != len(section):
            # section[x+1]에 접근하기 전에 x+1이 section의 길이보다 작은지 확인
            while (x+1 < len(section)) and ((section[x]+m-1) >= section[x+1]):
                del section[x+1]
        x += 1
        answer += 1
    return answer


