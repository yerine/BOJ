def solution(numbers, target):
    answer = 0

    cal_list = [numbers[0],-numbers[0]]
    for num in numbers[1:]:
        temp_list = list()
        for num2 in cal_list:
            temp_list.append(num2 + num)
            temp_list.append(num2 - num)

        cal_list = temp_list
    for num in cal_list:
        if num == target:
            answer += 1
            
    return answer