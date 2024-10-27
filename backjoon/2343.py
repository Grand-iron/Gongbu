n, m = input().split()
l = list(map(int, input().split()))

left =  max(l)
right = sum(l)

while left <= right:
    count = 0
    mid = (left + right) // 2
    total = 0
    for x in l:
        if (total + x) <= mid:
            total += x
        else:
            count += 1
            total = x
    
    if count < int(m):
        right = mid - 1
    else:
        left = mid + 1

print(left) 
