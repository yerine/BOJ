#import sys
#input = sys.stdin.readline

n = int(input())

members = {}
for i in range(n):
    age, name = input().split()
    age = int(age)
    if age in members.keys():
        members[age].append(name)
    else:
        members[age] = [name]
for age in sorted(members.keys()):
    for name in members[age]:
        print(age, name)


members[20]



print(''.join(sorted([*open(0)][1:],key=lambda x:int(x.split()[0]))))