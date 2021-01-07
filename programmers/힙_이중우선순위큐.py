import heapq

def solution(operations):
    answer = []
    
    for operation in operations:
        order, num = operation.split(" ")
        if order == "I":
            heapq.heappush(answer, int(num))
        elif len(answer) > 0:
            if num == "1":
                answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
            else:
                heapq.heappop(answer)
    
    if len(answer) == 0:
        return [0,0]
    else:
        return [heapq.nlargest(1,answer)[0], heapq.heappop(answer)]