n=100
total=0
list1=[]
for i in range(1,n+1):
    count=0
    list1=[]
    for j in range(1,i+1):
        if (i%j==0):
            count+=1
    if count==2:
        list1.append(i)
        total += i
print(total)

    



