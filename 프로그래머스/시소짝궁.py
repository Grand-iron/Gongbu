from collections import Counter


def solution(weights):
    answer = 0
    
    # 1:1
    count = Counter(weights)
    for k,v in count.items():
        if v>=2:
            answer+= v*(v-1)//2
    
    #중복제거
    weights = set(weights) 
    
    # 2:3 2:4 3:4 비율 가지면 짝궁 가능함
    for w in weights:
        if w*2/3 in weights:
            answer+= count[w*2/3] * count[w]
        if w*2/4 in weights:
            answer+= count[w*2/4] * count[w]
        if w*3/4 in weights:
            answer+= count[w*3/4] * count[w]
    return answer