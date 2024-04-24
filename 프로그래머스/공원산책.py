def solution(park, routes):
    가로=0
    세로=0
    공원가로=len(park[0])-1
    공원세로=len(park)-1
    for x in park:
        가로=0
        for y in x:
            if y=="S":
                위치=[세로,가로]
                break
            else:
                가로+=1
        세로+=1
    for x in routes:
        count=0
        for y in range(int(x[2])):
            if x[0]=="E":
                if 위치[1]+y+1<=공원가로:
                    if park[위치[0]][위치[1]+y+1]!="X":
                        count+=1
            elif x[0]=="N":
                if 위치[0]+(y*(-1))-1>=0:
                    if park[위치[0]+y*(-1)-1][위치[1]]!="X":
                        count+=1
            elif x[0]=="W":
                if 위치[1]+(y*(-1))-1>=0:
                    if park[위치[0]][위치[1]+y*(-1)-1]!= "X":
                        count+=1
            elif x[0]=="S":
                if 위치[0]+y+1<=공원세로:
                    print(위치[0])
                    if park[위치[0]+y+1][위치[1]]!="X":
                        count+=1
        if count==int(x[2]):
            if x[0]=="E":
                위치[1]+=int(x[2])
            elif x[0]=="N":
                위치[0]-=int(x[2])
            elif x[0]=="W":
                위치[1]-=int(x[2])
            elif x[0]=="S":
                위치[0]+=int(x[2])
    return 위치