# 방법1

word = list(input().upper())

alpha_dic = dict()
for i in word:
    if i in alpha_dic:
        alpha_dic[i] += 1
    else:
        alpha_dic[i] = 1

max_alpha = max(alpha_dic.values())

max_list = list()
for key, value in alpha_dic.items():
    if value == max_alpha:
        max_list.append(key)
        if len(max_list) > 1:
            break
        
if len(max_list) != 1:
    print('?')
else:
    print(max_list[0])
    
# 방법2
    
word = input().upper()

alpha_list = list()
max_num = 0
for i in range(26):
    character = chr(65+i)
    cnt_char = word.count(character)
    if cnt_char > max_num:
        max_num = cnt_char
    alpha_list.append(cnt_char)

if alpha_list.count(max_num) != 1:
    print('?')
else:
    max_idx = alpha_list.index(max_num)
    print(chr(65+max_idx))
