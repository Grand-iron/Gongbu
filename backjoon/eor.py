def solution(wallpaper):
    countx1=99
    county1=99
    countx2=-1
    county2=-1
    county=0
    countx=0
    for x in wallpaper: 
        countx=0
        if "#" in x and county1==99:
            county1=county
            print("county1=",county1)
        if "#" in x and county>=county2:
            county2=county
            print("county2=",county2)
        for y in x:
            if y=="#" and countx<=countx1:
                countx1=countx
                print("countx1=",countx1)
            if y=="#" and countx>=countx2:
                countx2=countx
                print("countx2=",countx2)
            countx+=1
        county+=1
    answer = [countx1,county1,countx2,county2]
    return answer

a=input()

print(solution(a))