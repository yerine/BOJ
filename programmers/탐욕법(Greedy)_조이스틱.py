def solution(name):
    answer = 0
    
    name_list = [91 - ord(alphabet) if alphabet > "M" else ord(alphabet) - 65 for alphabet in name]
    idx= 0
    while True:
        answer += name_list[idx]
        name_list[idx] = 0

        if sum(name_list) == 0:
            break

        left, right = 1, 1
        while name_list[idx - left] == 0:
            left += 1
        while name_list[idx + right] == 0:
            right += 1

        if left < right:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right
        
    return answer