def solution(arr):
    minNum = min(arr)
    if len(arr) == 1:
        return [-1]
    
    for i in range(0, len(arr)):
        if arr[i] == minNum:
            del arr[i]
            break
    return arr