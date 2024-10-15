def solution(n, words):
    play = []

    for key, value in enumerate(words):
        if len(play) == 0:
            play.append(value)
            continue
        if value[0] != play[-1][-1]:
            print(key)
            return [key % n + 1, (key) // n + 1]
        if play.count(value) != 0:
            print(key)
            return [key % n + 1, (key) // n + 1]
        play.append(value)
    
    return [0, 0]