def solution(sizes):
    countx=0
    county=0
    for x in sizes:
        a=0
        if x[0]<x[1]:
            a=x[0]
            x[0]=x[1]
            x[1]=a
        if countx<=x[0]:
            countx=x[0]
        if county<=x[1]:
            print(county,x[1])
            county=x[1]

    answer=countx*county
    return answer