def gcd(a, b):
    if b == 0:
        return '1'*a
    return gcd(b, a%b)

a, b = map(int, input().split())
print(gcd(a, b))
