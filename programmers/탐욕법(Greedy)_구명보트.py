def solution(people, limit):
    people.sort(reverse=True)
    h = 0
    t = len(people)-1
    while h < t:
        if  people[h] + people[t] <= limit:
            t -= 1
        h += 1

    return t + 1