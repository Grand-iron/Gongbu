def solution(friends, gifts):
    answer = 0
    #받을 선물 갯수 저장
    q=[0 for x in range(len(friends))]
    
    #갯수 저장
    a=[[] for x in range(len(friends))]
    for x in range(len(friends)):
        for y in range(len(friends)+1):   
            a[x].append(0)
    
    #카운팅
    for x in gifts:
        x=x.split()  
        a[friends.index(x[0])][friends.index(x[1])]+=1 #준거 카운팅
        
        #선물지수 카운팅
        a[friends.index(x[1])][len(friends)]-=1
        a[friends.index(x[0])][len(friends)]+=1
        
    for x in range(len(friends)):   
        for y in range(len(friends)):
            if a[x][y]!= 0: #선물을 줬다면
                if a[x][y] > a[y][x]: #준게 받은거 보다 많다면
                    q[x]+=1
                elif a[x][y] < a[y][x]:#받은게 준거보다 많다면
                    q[y]+=1
                else:
                    if a[x][len(friends)] > a[y][len(friends)]: #선물지수 비교
                        q[x]+=1
                    elif a[x][len(friends)] < a[y][len(friends)]: #선물지수 비교
                        q[y]+=1
            else:
                if a[y][x] ==0:              #둘다 안줬다면      
                    if a[x][len(friends)] > a[y][len(friends)]: #선물지수 비교
                        q[x]+=1
                    elif a[x][len(friends)] < a[y][len(friends)]: #선물지수 비교
                        q[y]+=1
                else:               #상대는 줬다면
                    q[y]+=1
    
    #가장 선물 많이 받을애 고르기    
    for x in q:
        if x/2>=answer:
            answer=x/2  
    return answer