def solution(arr):
    answer = []
    for i in range(0, len(arr)):
        if i == 0 or arr[i] != arr[i - 1]:
            answer.append(arr[i])
    return answer