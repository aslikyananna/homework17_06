name = input("write the name ")
tel_num = input("write the telephone number ")
names_list = list()
numbers_list = list()
names_list.append(name)
numbers_list.append(tel_num)
D = dict()
D = dict(zip(names_list, numbers_list))
search_name = input("writhe the name ")
if search_name in names_list:
    print(D[name])
else:
    print("the number do not found ")
print(D)
print("end of program ")



