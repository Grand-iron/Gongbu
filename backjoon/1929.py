a,b = map(int, input().split())

for x in range(a, b+1):
    if x == 1: 
        continue
        
    for y in range(2, int(x**0.5) + 1): 
        if x % y == 0: 
            break
    else: 
        print(x)