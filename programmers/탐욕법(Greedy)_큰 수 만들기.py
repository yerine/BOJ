def solution(n, lost, reserve): 
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for student in set_reserve:
        if student - 1 in set_lost:
            set_lost.remove(student - 1)
        elif student + 1 in set_lost:
            set_lost.remove(student + 1)
            
    return n - len(set_lost)