# In[1]:

def calculator(posfix, num_list):
    stack = []
    for i in posfix:
        if i.isupper():
            stack.append(num_list[ord(i)-65])        
        else:
            b = stack.pop()
            a = stack.pop()
            if i == '*':
                stack.append(a*b)
            elif i == '+':
                stack.append(a+b)
            elif i == '/':
                stack.append(a/b)
            elif i == '-':
                stack.append(a-b)
    
    return "%0.2f"%stack[0]

# In[2]:

n = int(input())
posfix = input()
num_list = [int(input()) for i in range(n)]
print(calculator(posfix, num_list))
