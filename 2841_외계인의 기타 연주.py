# In[0]:

from sys import stdin
input = stdin.readline

# In[1]:

def cntmove(n, p):
    result = 0
    finger = [[0] for i in range(n)]
    
    for i in range(n):
        line, fret = map(int, input().split())
    
        while len(finger[line-1]) > 0:
            if finger[line-1][-1] > fret:
                finger[line-1].pop()
                result += 1
            elif finger[line-1][-1] < fret:
                break
            else:
                finger[line-1].append(fret)
                result += 1
                break

    return result

# In[2]:
    
n, p = map(int, input().split())
print(cntmove(n, p))
