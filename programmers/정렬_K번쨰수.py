def solution(array, commands):
    return [sorted(array[a[0]-1:a[1]])[a[2]-1] for a in commands]

#다른 사람의 풀이

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))