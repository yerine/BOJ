a, b = map(int, input().split())
c = a*b

while b:
    a, b = b, a%b
    
print(a)
print(int(c/a))