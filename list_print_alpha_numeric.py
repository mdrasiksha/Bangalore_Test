list1 = ["1", 'abc12', 'abc', 'xyz12', '123']
for i in list1:
    if i.isalnum() and len(i) > 3:
        print(i)
