def solution(babbling):
    possible = 0
    possibleList = ["aya", "ye", "woo", "ma"]
    impossibleList = ["ayaaya", "yeye", "woowoo", "mama"]
    
    for word in babbling:
        for impos in impossibleList:
            if impos in word:
                word = word.replace(impos, "!")
        for pos in possibleList:
            if pos in word:
                word = word.replace(pos, " ")
        word = word.replace(' ','')
        if len(word) == 0:
            possible += 1
    
    return possible