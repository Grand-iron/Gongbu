import sys
try:
    n = int(sys.stdin.readline())
    answer = [int(sys.stdin.readline()) for _ in range(n)]
    stack = []
    rlt = []

    j = 0
    for i in range(1,n+1):
        stack.append(i)
        rlt.append('+')

        while j < n and answer[j] == stack[-1] :
            stack.pop()
            rlt.append('-')
            j += 1
            if not stack:
                break

    if stack:
        print('NO')
    else:
        for char in rlt:
            print(char)

except ValueError:
    print('Input Error')