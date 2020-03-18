#import sys
#input = sys.stdin.readline

t = int(input())

for i in range(t):
    result = "YES"
    
    left_stack = list()
    
    for i in list(input()):
        if i == "(":
            left_stack.append("(")
        elif i == ")":
            try:
                left_stack.pop()
            except:
                result = "NO"
                break
   
    if len(left_stack) != 0:
        result = "NO"
        
    print(result)