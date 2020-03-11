t = int(input())

for i in range(t):
    t, txt = input().split()
    t = int(t)
    for i in txt:
        print(i*t, end='')
    print()