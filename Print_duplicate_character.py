word = "welcome to my world"
list =[]
list1=[]
for i in word:
    if i not in list:
        list.append(i)
    else:
        list1.append(i)
print(list1)