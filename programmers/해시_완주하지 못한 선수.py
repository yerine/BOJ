def solution(participant, completion):
    answer = ''
    
    dic_part = {}
    for player in participant:
        if player not in dic_part:
            dic_part[player] = 0
        dic_part[player] += 1

    for player in completion:
        dic_part[player] -= 1
    
    for key, value in dic_part.items():
        if value > 0:
            answer = key
            break

    return answer

#다른 사람의 풀이

import collections

def solution(participant, completion):
    answer = list(collections.Counter(participant)-collections.Counter(completion))[0]
    return answer