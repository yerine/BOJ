# In[1]:

def editcnt(n, present, right):
    min_cnt = 0
    
    right_cnt = right.pop() - present.pop()
    for i in range(n-1):
        left_cnt = right.pop() - present.pop()
        if right_cnt * left_cnt <= 0:
            min_cnt += abs(right_cnt)
        elif left_cnt > 0:
            if left_cnt < right_cnt:
                min_cnt += right_cnt - left_cnt
        elif left_cnt < 0:
            if left_cnt > right_cnt:
                min_cnt -= right_cnt - left_cnt
        right_cnt = left_cnt
                
    if right_cnt > 0:
        min_cnt += right_cnt
    else:
        min_cnt -= left_cnt
    
    return min_cnt

# In[2]:
    
n = int(input())
present =list(map(int, input().split()))
right = list(map(int, input().split()))

print(editcnt(n, present, right))
