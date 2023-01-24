import sys
from collections import deque
n = int(sys.stdin.readline())
deck = list(map(int, sys.stdin.readline().split()))
count= deque()
for x in range(n):
    if deck[n-x-1] == 1:
        count.appendleft(x+1)
    elif deck[n-x-1] == 2:
        count.insert(1,x+1)
    elif deck[n-x-1] == 3:
        count.append(x+1)
for x in count:
    print(x,end=' ')