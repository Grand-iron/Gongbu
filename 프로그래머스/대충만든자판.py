def solution(keymap, targets):
    answer = []
    arr = [float("inf")] * 27

    for i, key in enumerate(keymap):
        for j, c in enumerate(key):
            idx = ord(c) - 65
            arr[idx] = min(arr[idx], j+1)
    print(arr)    

    for target in targets:
        result = 0

        for c in target:
            idx = ord(c) - 65
            result += arr[idx]
        if result == float('inf'):
            answer.append(-1)
        else:
            answer.append(result)

    return answer