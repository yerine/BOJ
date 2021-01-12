def solution(answers):
    p1 = [1, 2, 3, 4, 5] * 8
    p2 = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4
    answer_cnt = [0] * 3
    for i, ans in enumerate(answers):
        if p1[i % 40] == ans:
            answer_cnt[0] += 1
        if p2[i % 40] == ans:
            answer_cnt[1] += 1
        if p3[i % 40] == ans:
            answer_cnt[2] += 1

    return [i + 1 for i, j in enumerate(answer_cnt) if j == max(answer_cnt)]

# 다른 사람의 풀이

def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_cnt = [0] * 3
    for i, ans in enumerate(answers):
        if p1[i % len(p1)] == ans:
            answer_cnt[0] += 1
        if p2[i % len(p2)] == ans:
            answer_cnt[1] += 1
        if p3[i % len(p3)] == ans:
            answer_cnt[2] += 1
            
    return [i + 1 for i, j in enumerate(answer_cnt) if j == max(answer_cnt)]