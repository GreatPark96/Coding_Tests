def solution(n, arr1, arr2):
    result = [];
    for i in range(0, n):
        oper = arr1[i] | arr2[i]
        binStr = bin(oper).replace("0b","")
        if len(binStr) != n:
            for j in range(0, n - len(binStr)):
                binStr = "0" + binStr
        line = binStr.replace("1", "#")
        line = line.replace("0", " ")
        result.append(line)
    
    return result
  