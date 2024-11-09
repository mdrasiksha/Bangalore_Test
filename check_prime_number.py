# check prime number
'''num = int(input("enter number"))
count = 0
if num>1:
    for i in range(1,num+1):
        if (num%i) == 0:
            count = count + 111

    if count == 2:
        print("given no is prime number")
    else:
        print("give no not a prime number")'''
num = int(input("enter your number __"))
count = 0
for i in range(1,num+1):
    if (num%i)==0:
        count = count + 1
if count == 2:
    print("given number is prime number")
else:
    print("given number is not a prime number")
