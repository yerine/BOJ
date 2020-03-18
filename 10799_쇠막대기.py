#import sys
#input = sys.stdin.readline

cnt = 0
stack = []
for i in input().replace("()","*"):
   if i == "(":
       stack.append("(")
   elif i == ")":
       stack.pop()
       cnt += 1
   else:
       cnt += len(stack)
    
print(cnt)
