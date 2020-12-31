a, b, v = map(int, input().split())

d = 1
d += (v-a)//(a-b)
if (v-a) % (a-b):
    d += 1

print(d)
