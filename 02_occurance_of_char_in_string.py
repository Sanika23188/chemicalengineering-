#How to count number of letter in the string
from collections import Counter


my_string = "Hello World"
count = 0
for char in my_string:
    if char =="l":
        count += 1
        print(count)

for collection in my_string:
    count = Counter(my_string)
    print(count ["l"])



    
