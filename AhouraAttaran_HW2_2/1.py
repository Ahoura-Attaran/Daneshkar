my_str = input("Enter a line\n")

my_str = my_str.lower().split(" ")

ret_dic = {}
for w in my_str:
    if w not in ret_dic.keys():
        ret_dic[w] = 1
    
    else:
        ret_dic[w] += 1

print(ret_dic)