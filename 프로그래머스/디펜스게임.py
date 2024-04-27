import heapq

# def solution(n, k, enemy):
    
#     #라운드를 쭉 가면서 막힐때까지 리스트에 담아 그리고 막힐때 그 리스트의 max값과 비교를해서 큰수를 무적권을 쓴다.
#     road=[0]
#     answer = 0
#     for x in enemy:
#         if n >=x:
#             n-=x
#             road.append(x)
#             answer+=1
#         else:
#             if k >0:
#                 k-=1
#                 if max(road)>=x:
#                     n+=max(road)
#                     n-=x
#                     answer+=1
#                 else:
#                     answer+=1
#             else:
#                 return answer
#     # 50점밖에 안됬다.                
#     return answer

#그래서 질문게시판을 보니 힙큐를 사용해야지 시간 초과 및 오류가 안생긴다는 걸 깨닫고 수정하여 코드를 작성하였다.
def solution(n, k, enemy):
    answer = 0
    latest = 0

    heap = []
    # 무적권을 써서 회복하는 걸로
    for i, v in enumerate(enemy):
        n -= v
        heapq.heappush(heap, -v)
        if n < 0 :
            if k > 0:
                pre_v = -heapq.heappop(heap)
                n += pre_v #음수 전환후 회복
                k -= 1
                answer = i + 1
            else:
                answer = i 
                break
        else:
            answer = i + 1

    return answer