import heapq

def solution(scoville, K):  

    heapq.heapify(scoville)

    if scoville[0] >= K:
        return 0

    
    cnt = 0
    while len(scoville) != 1:
        i,j = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, i + j*2)
        cnt += 1
        if scoville[0] >= K :
            return cnt
        
    
    return -1