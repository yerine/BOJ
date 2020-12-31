#import sys
#input = sys.stdin.readline

num = 1
seq = []
result = ''
for i in range(int(input())):
    num_seq = int(input())
    
    while num <= num_seq:
        seq.append(num)
        result += "+\n"
        num += 1
        
    if seq[-1] == num_seq:
        seq.pop()
        result += "-\n"
    else:
        result = "NO"
        break

print(result.strip())