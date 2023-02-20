num=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
a=list(input())
clock=0
for q in a:
    count=2
    for x in num:
        count+=1
        for y in x:
            if q==y:
                clock+=count
print(clock)