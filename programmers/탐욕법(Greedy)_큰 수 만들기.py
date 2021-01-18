def solution(number, k):
    number = list(number)
    answer = [number.pop(0)]

    for elem in number:
        while answer and elem > answer[-1] and k > 0:
            answer.pop()
            k -= 1

        answer.append(elem)

    while k > 0:
        answer.pop()
        k -= 1

    answer = "".join(answer)
    
    return answer