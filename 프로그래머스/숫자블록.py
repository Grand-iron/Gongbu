def solution(begin, end):
    answer = []
    for x in range(begin,end+1):    
        i=2 
        if x==1:            
            answer.append(0)
        else:
            q=[1]                     
            for i in range(2, int(x**(1/2)) + 1):   #i값을 2부터 x-1까지 1씩 올려가며 x값을 나눈다.  
                if (x % i == 0) and i <= 10000000:       #나머지값이 0이다 = 약수 1 2 4 8 16 2투입
                    q.append(i)  
                    if x//i <= 10000000 and x//i != x:   # ex: 1 2 4 8 16 2투입 8투입 4는 겹이기에 투입 막는 중  
                        q.append((x // i))
            answer.append(max(q))
            
    return answer