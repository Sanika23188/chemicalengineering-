# How to convert list to dictionary
# Two methods to convert list to dictionary

# 1 zip method
key_list = ["Name","Age","Gender"]
value_list = ["Rohan","25","Male"]
my_dict = dict(zip(key_list, value_list))
print(my_dict)

# 2 loop method
i=0
my_dict = {}
for ikey in key_list:
    my_dict[ikey] = value_list[i]
    i +=1



