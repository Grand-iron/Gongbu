def solution(absolutes, signs):
    answer=0
    for x in range(len(absolutes)):
        if signs[x] == True:
            answer+=absolutes[x]
        else:
            answer-=absolutes[x]
    return answer