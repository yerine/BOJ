def solution(clothes):
    answer = 1
    
    num_clothes = {}
    for item in clothes:
        num_clothes[item[1]] = num_clothes.get(item[1], 0) + 1
    for num in num_clothes.values():
        answer *= (num + 1)
        
    return answer - 1

#다른 사람의 풀이

import collections
from functools import reduce

def solution(c):
    return reduce(lambda x,y:x*y,[a+1 for a in collections.Counter([x[1] for x in c]).values()])-1