word = input()

num_list = []
for i in word:
    i_ord = ord(i)
    if i_ord <= 79:
        num = (ord(i)+1)//3 - 20
    elif i_ord <= 83:
        num = 7
    elif i_ord <= 86:
        num = 8
    else:
        num = 9
    num_list.append(num)

time = sum(num_list) + len(num_list)
print(time)