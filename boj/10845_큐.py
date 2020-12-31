# In[0]:

#import sys
#input = sys.stdin.readline

# In[1]:

queue = []
for i in range(int(input())):
    command = input().rstrip()
    if 'push' in command:
        command, num = command.split()
        queue.append(num)
    elif command == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
