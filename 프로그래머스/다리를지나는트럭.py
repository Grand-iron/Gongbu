def solution(bridge_length, weight, truck_weights):
    num=0
    count=0
    a=[0 for x in range(bridge_length)]  #다리 대기열 표현 
    while(len(truck_weights)!=0): #대기트럭이 없을때까지
        num-=a.pop(0)           #대기열 앞에 빼고 
        if num+truck_weights[0]<=weight: #weight내일시 대기트럭 추가 아닐시 0추가
            b=truck_weights.pop(0)
            a.append(b)
            num+=b
        else:
            a.append(0)
        count+=1               #시간 카운팅
    count+=len(a)              #마지막 대기트럭 들어가고 대기트럭이 다리 건날시간 추가
    return count