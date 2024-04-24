def solution(friends, gifts):
    answer = 0
    #총 내가 받은 개수와 준 개수를 구해야함 이걸 이용해서 선물지수를 구할 수 있다.
    #내가 누구를 줬는지를 알아야함 누구를 줬다면? 걔가 그사람한테 얼마나줬는지를 비교하고 이게 같으면 선물지수 비교
    #                         안줬다면? 걔가 그사람한테 주었는지에 따라 비교
    
    #a b c [0,0,0]
    #[3,1,2,0] a
    #[1,1,0,0] b
    #[2,0,2,0] c
    
    # 
    # a b=1발견 > b a=1발견 > 선물지수 같음 즉 노 교환  
    
    #갯수 저장기 
    a=[[] for x in range(len(friends))]
    for x in range(len(friends)):
        for y in range(len(friends)+1):   
            a[x].append(0)
    
    #카운팅
    for x in gifts:
        print(x)
        x.split()
        a[friends.index(x[0])][friends.index(x[1])]+=1
    print(a)
    return answer

gifts= ["a b", "b a", "c a", "a c", "a c", "c a"]
friends= ["a", "b", "c"]
gifts[0].split()
print(gifts[0].split())