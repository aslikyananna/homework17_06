L = {}
while True:
    choice = input("if you want \n"
                   "Add a new contact press 1 \n"
                   "Search for a contact press 2 \n"
                   "List all contacts press 3 \n"
                   "Exit 4 ")
    if choice == 1:
        name = input("Add the name: ")
        phone_num = int(input("add phone numb" ))
        L[name] = phone_num
    elif choice == 2:
        search_name = input("writhe the name ")
        if search_name in L.keys():
            print(L[search_name])
        else:
            print("the number do not found ")
    elif choice == 3:
        print(L)
    elif choice == 4:
        print("end")
    else:
        print("write a correct symbol")
