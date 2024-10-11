def solution(s):
    open = 0
    
    for i in range(0, len(s)):
        if open <= 0 and s[i] == ")":
            return False
        if s[i] == "(":
            open += 1
        else:
            open -= 1
    
    if open == 0:
        return True
    else:
        return False