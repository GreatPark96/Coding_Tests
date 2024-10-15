def solution(s):
    
    stck = []
    
    for i in range(0, len(s)):
        if not stck:
            stck.append(s[i])
            continue
            
        top = stck[-1]
        if top == s[i]:
             stck.pop()
        else:
            stck.append(s[i])
        
    return 1 if not stck else 0




