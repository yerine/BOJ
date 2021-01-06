import heapq
import numpy as np

def solution(jobs):
    answer = 0
    heapq.heapify(jobs)
    n = len(jobs)

    curr_time = 0
    pos_jobs = []
    while jobs:
        while jobs and jobs[0][0] <= curr_time:
            pos_jobs.append(heapq.heappop(jobs))

        if pos_jobs:
            pos_jobs.sort(reverse = True, key = lambda x : x[1])
            curr_job = pos_jobs.pop()
            curr_time += curr_job[1]
            answer += (curr_time - curr_job[0])
        else:
            curr_time += 1

    while pos_jobs:
        curr_job = pos_jobs.pop()
        curr_time += curr_job[1]
        answer += curr_time - curr_job[0]
    
    return answer // n

# 해당시점에서 시행할 수 있는 작업중 소요시간이 가장 짧은 것 부터 수행