#import sys
#input = sys.stdin.readline
import re

sentence = input().rstrip("\n")
while sentence != ".":
    result = "yes"
    left_stack = []
    for i in re.findall("[\(\)\[\]]",sentence):
        if i == "(" or i == "[":
            left_stack.append(i)
        elif i == ")":
            try:
                if left_stack.pop() != "(":
                    result = "no"
                    break
            except:
                result = "no"
                break
        elif i == "]":
            try:
                if left_stack.pop() != "[":
                    result = "no"
                    break
            except:
                result = "no"
                break
  
    if len(left_stack) != 0:
        result = "no"
            
    print(result, '출력')
    sentence = input()
                