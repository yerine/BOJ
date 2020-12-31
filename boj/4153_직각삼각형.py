x, y, z = map(int, input().split())

while x != 0:
    x2 = x**2; y2 = y**2; z2 = z**2
    if 2 * max(x2, y2, z2) == x2 + y2 + z2:
        print("right")
    else:
        print("wrong")
        
    x, y, z = map(int, input().split())