def solution(prices):
    answer = [0] * len(prices)
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
                
    return answer

#다른 사람의 풀이

def solution(prices):
    answer = [0]*len(prices)
    
    stack = []
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
 
    return answer