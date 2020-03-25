# In[1]:

import collections

cards = collections.deque([i for i in range(1, int(input())+1)])

while len(cards) != 1:
    cards.popleft()
    cards.append(cards.popleft())
    
print(cards[0])

# In[2]:

n = int(input())
power = 1

while 2**power < n:
    power += 1

print(1 if n==1 else 2*n-2**power)
