n = int(input())

num = 0
for i in range(n):
    word = input()
    num_alpha = len(set(word))
    num_change = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            num_change += 1
    if num_alpha - num_change ==1:
        num += 1

print(num)