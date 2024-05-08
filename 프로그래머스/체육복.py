def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    lost2=lost.copy()
    count=len(lost)
    for x in lost2:
        if x in reserve:
            reserve.pop(reserve.index(x))
            count-=1
            lost.pop(lost.index(x))
    for x in lost:
        if x-1 in reserve:
            reserve.pop(reserve.index(x-1))
            count-=1
        elif x+1 in reserve:
            reserve.pop(reserve.index(x+1))
            count-=1
    return answer-count