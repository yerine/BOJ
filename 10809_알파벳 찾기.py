word = input()

for i in range(25):
    character = chr(97+i)
    print(word.find(character), end=' ')
print(word.find('z'))
