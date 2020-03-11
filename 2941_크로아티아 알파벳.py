alphabet = input()

a = alphabet.count('=')
a1 = alphabet.count('dz=')
b = alphabet.count('-')
c1 = alphabet.count('lj')
c2 = alphabet.count('nj')

print(len(alphabet)-a-a1-b-c1-c2)
