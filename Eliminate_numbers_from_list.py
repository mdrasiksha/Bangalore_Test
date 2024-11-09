list1 = [1,2,3,4,5]
list2 = []
for i in list1:
    if i==2 or i==4:
        continue
    else:
        list2.append(i)
print(list2)
