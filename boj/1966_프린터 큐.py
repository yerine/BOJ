# In[1]:

def printer(n, m, importance):
    result = 0
    while 1:
        maximum = max(importance)
        temp = importance.pop(0)
        if temp != maximum:
            importance.append(temp)
        else:
            result += 1
            if m == 0:
                return result
            n -= 1
            pass
        m = (m-1) % n
        
# In[2]:
        
for i in range(int(input())):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    print(printer(n,m,importance))
