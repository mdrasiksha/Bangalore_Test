n = 11
count = 0
for i in range(1,11):
    if (n%i)==0:
        count = count + 1
if count == 2:
    print("given number is prime number")
else:
    print("not a prime number")


