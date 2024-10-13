def solution(s):
    upper = []
    lower = []
    
    for c in s:
        if c.isupper():
            upper.append(c)
        elif c.islower():
            lower.append(c)
            

    lower.sort(reverse = True)
    sortLower = "".join(lower)

    upper.sort(reverse = True)
    sortUpper = "".join(upper)

    return sortLower + sortUpper