def solution(s):
    splitList = s.split(" ")
    words = []
    
    for w in splitList:
        wordList = list(w)
        word = []
        for i in range(0, len(wordList)):
            if i == 0:
                word.append(wordList[i].upper())
                continue
            if wordList[i] == " ":
                continue
            if i % 2 == 0:
                 word.append(wordList[i].upper())
            else:
                 word.append(wordList[i].lower())
        words.append("".join(word))
    return " ".join(words)
        
        
        
        

            
    
    return "".join(s)