import math 

def solution(progresses, speeds):
    answer = []
    period = 0
    for p, s in zip(progresses, speeds):
        temp = math.ceil((100 - p) / s)
        if temp > period:
            answer.append(1)
            period = temp
        else:
            answer.append(answer.pop() + 1)
    return answer