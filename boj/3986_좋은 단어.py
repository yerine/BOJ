# In[1]:

def goodword(word):
    if len(word)%2 != 0 or word.count('A')%2 != 0:
        return False
    
    stack = list()
    for i in range(len(word)):
        if len(stack) == 0:
            stack.append(word[i])
            continue
        
        if stack[-1] == word[i]:
            stack.pop()
        else:
            stack.append(word[i])
            
    if len(stack) == 0:
        return True
    else:
        return False

# In[2]:
    
def goodword(word):
    if len(word)%2 != 0 or word.count('A')%2 != 0:
        return False
    
    while word != '':
        temp = word.replace('AA','').replace('BB','')
        
        if temp == word:
            return False
        else:
            word = temp
        
    return True

# In[3]:
    
result = 0
for i in range(int(input())):
    if goodword(input()):
        result += 1

print(result)
