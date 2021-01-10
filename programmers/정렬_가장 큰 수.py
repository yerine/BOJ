def solution(numbers):
    if not sum(numbers):
        return "0"
    return ''.join(sorted(list(map(str, numbers)), key = lambda x: x * 3, reverse = True))