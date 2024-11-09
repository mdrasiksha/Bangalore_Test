txt = "wellwehsfhgfdhfsdh"
count=[0]
for i in txt:
    if i not in count:
        count += i
    else:
        print(i,end="")