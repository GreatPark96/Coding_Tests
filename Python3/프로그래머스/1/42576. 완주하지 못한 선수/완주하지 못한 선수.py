def solution(participant, completion):
    hashMap = {}
    for person in participant:
        hashMap[person] = hashMap.get(person, 0) + 1
    for person in completion:
        hashMap[person] -= 1
    for key, value in hashMap.items():
        if value > 0:
            return key
    