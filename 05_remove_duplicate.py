# How to remove duplicate from the list
# we have three methods
my_list = ["A","B","C","D","A"]
N_list = []
for ichar in my_list:
    if ichar not in N_list:
        N_list.append(ichar)
        print(N_list)

# 2 set method
print(list(set(my_list)))

# 3 dictionary method
print(list(dict.fromkeys(my_list)))
        