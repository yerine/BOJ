#import sys
#input = sys.stdin.readline

max_num = 0
max_index = 0

for i in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        max_index = i + 1
        
print("%s\n%s"%(max_num, max_index))