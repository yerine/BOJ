def sum_ab(a, b):
    if a <= b:
        return (a+b) * (b-a+1) // 2
    else:
        return (a+b) * (a-b+1) // 2
    
a, b = map(int, input().split())
print(sum_ab(a, b))
