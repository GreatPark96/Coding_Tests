def solution(arr1, arr2):
    answer = []

    for i in range(0, len(arr1)):
        sumList = []
        for j in range(0, len(arr1[i])):
            sumList.append(arr1[i][j] + arr2[i][j])
        answer.append(sumList)
    return answer