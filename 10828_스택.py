#import sys
#input = sys.stdin.readline

n = int(input())

lst = []
for i in range(n):
    func = input().split()
    
    if func[0] == 'push':
        lst.append(func[1])
    elif func[0] == 'pop':
        if len(lst) != 0:
            print(lst.pop())
        else:
            print(-1)
    elif func[0] == 'size':
        print(len(lst))
    elif func[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif func[0] == 'top':
        if len(lst) != 0:
            print(lst[-1])
        else:
            print(-1)